# main_gui.py

import sys
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Backend import
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))
from menu import menu_items

# -------------------------------------------------
# Globals
# -------------------------------------------------
order = {}
ORIGINAL_IMAGES = {}
PHOTO_CACHE = {}

CARD_PADX = 10
CARD_PADY = 10
CARD_MIN_WIDTH = 180
CARD_MIN_HEIGHT = 180
IMAGE_RATIO = 0.75

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
PLACEHOLDER = os.path.join(ASSETS_DIR, "placeholder.png")

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def asset_path_for_item(item):
    base = item.get("image")
    if base:
        full = os.path.join(ASSETS_DIR, base)
        if os.path.exists(full):
            return full
    name = item.get("name", "").lower().replace(" ", "_") + ".png"
    full = os.path.join(ASSETS_DIR, name)
    if os.path.exists(full):
        return full
    if os.path.exists(PLACEHOLDER):
        return PLACEHOLDER
    return None

def load_original_image(path):
    if not path or not os.path.exists(path):
        return None
    if path in ORIGINAL_IMAGES:
        return ORIGINAL_IMAGES[path]
    try:
        img = Image.open(path).convert("RGBA")
        ORIGINAL_IMAGES[path] = img
        return img
    except:
        return None

def get_resized_photo(path, w, h):
    if not path or w <= 0 or h <= 0:
        return None
    key = (path, w, h)
    if key in PHOTO_CACHE:
        return PHOTO_CACHE[key]
    orig = load_original_image(path)
    if orig is None:
        return None
    ow, oh = orig.size
    ratio = min(w / ow, h / oh)
    new_w, new_h = int(ow * ratio), int(oh * ratio)
    resized = orig.resize((new_w, new_h), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized)
    PHOTO_CACHE[key] = photo
    return photo

# -------------------------------------------------
# Order Management
# -------------------------------------------------
def add_to_order(item):
    iid = item["id"]
    if iid in order:
        order[iid]["quantity"] += 1
    else:
        order[iid] = {"item": item, "quantity": 1}
    refresh_order_panel()

def calculate_total():
    return sum(v["item"]["price"] * v["quantity"] for v in order.values())

def refresh_order_panel():
    for widget in order_items_frame.winfo_children():
        widget.destroy()
    for iid, v in order.items():
        it = v["item"]
        qty = v["quantity"]
        subtotal = it["price"] * qty

        item_frame = tk.Frame(order_items_frame, bg="#2b2b2b")
        item_frame.pack(fill="x", pady=4, padx=5)

        # Image
        path = asset_path_for_item(it)
        photo = get_resized_photo(path, 60, 60)
        if photo:
            img_lbl = tk.Label(item_frame, image=photo, bg="#2b2b2b")
            img_lbl.image = photo
            img_lbl.pack(side="left", padx=5)
        else:
            tk.Label(item_frame, text="No Img", bg="#2b2b2b", fg="white", width=8).pack(side="left", padx=5)

        # Text info
        tk.Label(item_frame, text=f"{it['name']} x {qty} - ₱{subtotal}", bg="#2b2b2b",
                 fg="white", font=("Helvetica", 12, "bold"), anchor="w").pack(side="left", fill="x")

        # Controls
        ctrl_frame = tk.Frame(item_frame, bg="#2b2b2b")
        ctrl_frame.pack(side="right", padx=5)

        tk.Button(ctrl_frame, text="+", width=2, command=lambda iid=iid: increase_item(iid)).pack(side="left", padx=1)
        tk.Button(ctrl_frame, text="-", width=2, command=lambda iid=iid: decrease_item(iid)).pack(side="left", padx=1)
        tk.Button(ctrl_frame, text="Remove", width=6, command=lambda iid=iid: remove_item(iid)).pack(side="left", padx=1)

    total_label.config(text=f"Total: ₱{calculate_total()}")

def increase_item(iid):
    order[iid]["quantity"] += 1
    refresh_order_panel()

def decrease_item(iid):
    order[iid]["quantity"] -= 1
    if order[iid]["quantity"] <= 0:
        del order[iid]
    refresh_order_panel()

def remove_item(iid):
    del order[iid]
    refresh_order_panel()

def on_checkout():
    if not order:
        messagebox.showinfo("Checkout", "No items in order.")
        return
    receipt = "---- PULP Receipt ----\n"
    for cat in menu_items.keys():
        cat_items = [v for v in order.values() if v["item"] in menu_items[cat]]
        if cat_items:
            receipt += f"\n{cat}:\n"
            for v in cat_items:
                it = v["item"]
                qty = v["quantity"]
                subtotal = it["price"] * qty
                receipt += f"{it['name']} x {qty} - ₱{subtotal}\n"
    receipt += f"\nTotal: ₱{calculate_total()}\nThank you for your order!"
    messagebox.showinfo("Receipt", receipt)
    order.clear()
    refresh_order_panel()

# -------------------------------------------------
# Card Events
# -------------------------------------------------
def card_on_click(frame, item, selected):
    if not selected.get():
        frame.config(highlightthickness=3, highlightbackground="#000000")
        selected.set(True)
    else:
        frame.config(highlightthickness=1, highlightbackground="#cccccc")
        selected.set(False)
    add_to_order(item)

# -------------------------------------------------
# Responsive Layout
# -------------------------------------------------
def compute_columns(width):
    min_card = CARD_MIN_WIDTH + CARD_PADX * 2
    return max(1, width // min_card)

def rebuild_menu_grid(event=None):
    menu_frame.update_idletasks()
    w = menu_frame.winfo_width()
    cols = compute_columns(max(300, w))
    for widget in menu_inner.winfo_children():
        widget.destroy()
    PHOTO_CACHE.clear()
    row = 0
    for category, items in menu_items.items():
        tk.Label(menu_inner, text=category, font=("Helvetica", 14, "bold"),
                 bg="black", fg="white").grid(row=row, column=0, columnspan=cols, sticky="w", pady=(10,4))
        row += 1
        col = 0
        for item in items:
            card = tk.Frame(menu_inner, bg="white",
                            highlightthickness=1, highlightbackground="#cccccc",
                            bd=2, relief="ridge")
            card.grid(row=row, column=col, padx=CARD_PADX, pady=CARD_PADY, sticky="n")
            card_width = max(CARD_MIN_WIDTH, (w - (cols+1)*CARD_PADX)//cols)
            img_h = int(card_width * IMAGE_RATIO)
            img_w = card_width - 20
            path = asset_path_for_item(item)
            photo = get_resized_photo(path, img_w, img_h)
            if photo:
                img_lbl = tk.Label(card, image=photo, bg="white")
                img_lbl.image = photo
            else:
                img_lbl = tk.Label(card, text=item["name"], bg="#eeeeee", width=20, height=8)
            img_lbl.pack(padx=10, pady=(10,6))
            tk.Label(card, text=item["name"], font=("Helvetica", 12, "bold"), bg="white").pack()
            tk.Label(card, text=f"₱{item['price']}", font=("Helvetica", 11), bg="white").pack(pady=(0,8))
            selected = tk.BooleanVar(value=False)
            for widget in (card, img_lbl):
                widget.bind("<Button-1>", lambda e, f=card, it=item, s=selected: card_on_click(f, it, s))
            col += 1
            if col >= cols:
                col = 0
                row += 1
        row += 1
    menu_inner.update_idletasks()

# -------------------------------------------------
# MAIN WINDOW
# -------------------------------------------------
root = tk.Tk()
root.title("PULP")
root.geometry("1200x700")
root.minsize(700, 500)
root.configure(bg="black")

# Header
header = tk.Frame(root, bg="black")
header.pack(fill="x", padx=20, pady=10)
logo_path = os.path.join(ASSETS_DIR, "logo.png")
if os.path.exists(logo_path):
    img = load_original_image(logo_path)
    if img:
        logo_photo = ImageTk.PhotoImage(img.resize((160, 160), Image.LANCZOS))
        tk.Label(header, image=logo_photo, bg="black").pack(expand=True)
        header.image = logo_photo

# Content
content = tk.Frame(root, bg="black")
content.pack(fill="both", expand=True, padx=20, pady=10)
content.grid_rowconfigure(0, weight=1)
content.grid_columnconfigure(0, weight=3)
content.grid_columnconfigure(1, weight=1)

# Menu Section
menu_container = tk.Frame(content, bg="black")
menu_container.grid(row=0, column=0, sticky="nsew", padx=(0,10))
menu_frame = menu_container
menu_canvas = tk.Canvas(menu_container, bg="black", highlightthickness=0)
menu_scrollbar = tk.Scrollbar(menu_container, orient="vertical", command=menu_canvas.yview)
menu_canvas.configure(yscrollcommand=menu_scrollbar.set)
menu_scrollbar.pack(side="right", fill="y")
menu_canvas.pack(side="left", fill="both", expand=True)
menu_inner = tk.Frame(menu_canvas, bg="black")
menu_canvas.create_window((0,0), window=menu_inner, anchor="nw")
menu_inner.bind("<Configure>", lambda e: menu_canvas.configure(scrollregion=menu_canvas.bbox("all")))
menu_frame.bind("<Configure>", rebuild_menu_grid)

# Order Panel
order_panel = tk.Frame(content, bg="#1e1e1e", bd=2, relief="ridge", highlightthickness=1, highlightbackground="#555555")
order_panel.grid(row=0, column=1, sticky="nsew")

tk.Label(order_panel, text="Your Order", font=("Helvetica", 14, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)

# Scrollable frame for items
order_items_container = tk.Frame(order_panel, bg="#2b2b2b")
order_items_container.pack(fill="both", expand=True, padx=5, pady=(0,5))

order_canvas = tk.Canvas(order_items_container, bg="#2b2b2b", highlightthickness=0)
order_scrollbar = tk.Scrollbar(order_items_container, orient="vertical", command=order_canvas.yview)
order_canvas.configure(yscrollcommand=order_scrollbar.set)

order_scrollbar.pack(side="right", fill="y")
order_canvas.pack(side="left", fill="both", expand=True)

order_items_frame = tk.Frame(order_canvas, bg="#2b2b2b")
order_canvas.create_window((0,0), window=order_items_frame, anchor="nw")

def on_frame_configure(event):
    order_canvas.configure(scrollregion=order_canvas.bbox("all"))

order_items_frame.bind("<Configure>", on_frame_configure)

def _on_mousewheel(event):
    order_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

order_canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Bottom frame for total and checkout
order_bottom_frame = tk.Frame(order_panel, bg="#1e1e1e")
order_bottom_frame.pack(fill="x", side="bottom", pady=10)

total_label = tk.Label(order_bottom_frame, text="Total: 0", font=("Helvetica", 12, "bold"), bg="#1e1e1e", fg="white")
total_label.pack(side="left", padx=10)

checkout_btn = tk.Button(order_bottom_frame, text="Checkout", bg="white", fg="black", width=15, relief="raised", bd=2, command=on_checkout)
checkout_btn.pack(side="right", padx=10)

# Initial build
root.after(300, rebuild_menu_grid)

root.mainloop()
