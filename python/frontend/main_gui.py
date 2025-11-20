# main_gui.py

import sys
import os

# Fix backend import
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))
from menu import menu_items  # now works

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# -------------------------------------------------
# Globals
# -------------------------------------------------

order = {}
ORIGINAL_IMAGES = {}
PHOTO_CACHE = {}
CARD_WIDGETS = {}

CARD_PADX = 10
CARD_PADY = 10
CARD_MIN_WIDTH = 180
CARD_MIN_HEIGHT = 180
IMAGE_RATIO = 0.75

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
PLACEHOLDER = os.path.join(ASSETS_DIR, "placeholder.png")

# -------------------------------------------------
# Image Helpers (Safe Version)
# -------------------------------------------------

def asset_path_for_item(item):
    """Return the path to the item's image, or placeholder if missing."""
    base = item.get("image")
    if base:
        full = os.path.join(ASSETS_DIR, base)
        if os.path.exists(full):
            return full
        else:
            print(f"Warning: Image not found for item '{item['name']}': {base}")

    # Try filename from item name
    name = item.get("name", "").lower().replace(" ", "_") + ".png"
    full = os.path.join(ASSETS_DIR, name)
    if os.path.exists(full):
        return full

    import re
    cleaned = re.sub(r'[^a-z0-9_]', '', item.get("name", "").lower().replace(" ", "_")) + ".png"
    full2 = os.path.join(ASSETS_DIR, cleaned)
    if os.path.exists(full2):
        return full2

    # fallback placeholder
    if os.path.exists(PLACEHOLDER):
        return PLACEHOLDER

    print(f"Warning: No image found for '{item['name']}', and placeholder missing!")
    return None

def load_original_image(path):
    """Load image safely. Returns None if it fails."""
    if not path or not os.path.exists(path):
        print(f"Warning: Cannot load image: {path}")
        return None
    if path in ORIGINAL_IMAGES:
        return ORIGINAL_IMAGES[path]
    try:
        img = Image.open(path).convert("RGBA")
        ORIGINAL_IMAGES[path] = img
        return img
    except Exception as e:
        print(f"Error loading image '{path}': {e}")
        return None

def get_resized_photo(path, w, h):
    """Resize image safely and return PhotoImage. Returns None if image is missing."""
    key = (path, w, h)
    if key in PHOTO_CACHE:
        return PHOTO_CACHE[key]

    orig = load_original_image(path)
    if orig is None:
        return None

    try:
        ow, oh = orig.size
        ratio = min(w / ow, h / oh)
        new_w = int(ow * ratio)
        new_h = int(oh * ratio)
        resized = orig.resize((new_w, new_h), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized)
        PHOTO_CACHE[key] = photo
        return photo
    except Exception as e:
        print(f"Error resizing image '{path}': {e}")
        return None

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

def decrease_quantity(iid):
    if iid in order:
        order[iid]["quantity"] -= 1
        if order[iid]["quantity"] <= 0:
            del order[iid]
    refresh_order_panel()

def remove_item_from_order(iid):
    if iid in order:
        del order[iid]
    refresh_order_panel()

def calculate_total():
    return sum(v["item"]["price"] * v["quantity"] for v in order.values())

# -------------------------------------------------
# Order Panel Updates
# -------------------------------------------------

def refresh_order_panel():
    order_listbox.delete(0, tk.END)

    for v in order.values():
        it = v["item"]
        qty = v["quantity"]
        subtotal = it["price"] * qty
        order_listbox.insert(tk.END, f"{it['name']} x {qty} - {subtotal}")

    total_label.config(text=f"Total: {calculate_total()}")

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
                receipt += f"{it['name']} x {qty} - {subtotal}\n"

    receipt += f"\nTotal: {calculate_total()}\nThank you for your order!"
    messagebox.showinfo("Receipt", receipt)

    order.clear()
    refresh_order_panel()

# -------------------------------------------------
# Card Events
# -------------------------------------------------

def card_on_enter(event, frame):
    frame.config(highlightthickness=2, highlightbackground="#222222")

def card_on_leave(event, frame, selected):
    if not selected.get():
        frame.config(highlightthickness=1, highlightbackground="#cccccc")

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
        tk.Label(
            menu_inner,
            text=category,
            font=("Helvetica", 14, "bold"),
            bg=menu_inner["bg"]
        ).grid(row=row, column=0, columnspan=cols, sticky="w", pady=(10, 4))

        row += 1
        col = 0

        for item in items:
            card = tk.Frame(menu_inner, bg="white",
                            highlightthickness=1, highlightbackground="#cccccc")
            card.grid(row=row, column=col, padx=CARD_PADX, pady=CARD_PADY, sticky="n")

            card_width = max(CARD_MIN_WIDTH, (w - (cols + 1) * CARD_PADX) // cols)
            img_h = int(card_width * IMAGE_RATIO)
            img_w = card_width - 20

            path = asset_path_for_item(item)
            photo = get_resized_photo(path, img_w, img_h)

            if photo:
                img_lbl = tk.Label(card, image=photo, bg="white")
                img_lbl.image = photo
            else:
                img_lbl = tk.Label(card, text=item["name"], bg="#eeeeee", width=20, height=8)

            img_lbl.pack(padx=10, pady=(10, 6))

            tk.Label(card, text=item["name"],
                     font=("Helvetica", 12, "bold"), bg="white").pack()
            tk.Label(card, text=f"₱{item['price']}",
                     font=("Helvetica", 11), bg="white").pack(pady=(0, 8))

            selected = tk.BooleanVar(value=False)

            for widget in (card, img_lbl):
                widget.bind("<Enter>", lambda e, f=card: card_on_enter(e, f))
                widget.bind("<Leave>", lambda e, f=card, s=selected: card_on_leave(e, f, s))
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
root.title("PULP - The raw element")
root.geometry("1200x700")
root.minsize(700, 500)
root.configure(bg="white")

# Header
header = tk.Frame(root, bg="white")
header.pack(fill="x", padx=20, pady=10)

logo_path = os.path.join(ASSETS_DIR, "logo.png")
if os.path.exists(logo_path):
    img = load_original_image(logo_path)
    if img:
        small = img.resize((90, 90), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(small)
        lbl = tk.Label(header, image=logo_photo, bg="white")
        lbl.image = logo_photo
        lbl.pack(side="left", padx=(0, 10))
else:
    tk.Label(header, text="PULP", font=("Helvetica", 20, "bold"), bg="white").pack(side="left")

tk.Label(header, text="PULP - The raw element",
         font=("Helvetica", 18), bg="white").pack(side="left")

# Main Content
content = tk.Frame(root, bg="white")
content.pack(fill="both", expand=True, padx=20, pady=10)

content.grid_rowconfigure(0, weight=1)
content.grid_columnconfigure(0, weight=3)
content.grid_columnconfigure(1, weight=1)

# Menu Section
menu_container = tk.Frame(content, bg="white")
menu_container.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

menu_frame = menu_container
menu_canvas = tk.Canvas(menu_container, bg="white", highlightthickness=0)
menu_scrollbar = tk.Scrollbar(menu_container, orient="vertical", command=menu_canvas.yview)
menu_canvas.configure(yscrollcommand=menu_scrollbar.set)

menu_scrollbar.pack(side="right", fill="y")
menu_canvas.pack(side="left", fill="both", expand=True)

menu_inner = tk.Frame(menu_canvas, bg="white")
menu_canvas.create_window((0, 0), window=menu_inner, anchor="nw")

# Order Panel
order_panel = tk.Frame(content, bg="#f8f8f8", bd=1, relief="solid")
order_panel.grid(row=0, column=1, sticky="nsew")

tk.Label(order_panel, text="Your Order",
         font=("Helvetica", 14, "bold"), bg="#f8f8f8").pack(pady=10)

order_listbox = tk.Listbox(order_panel, width=40, height=15, font=("Helvetica", 12))
order_listbox.pack(padx=10, pady=5)

# Controls
controls = tk.Frame(order_panel, bg="#f8f8f8")
controls.pack()

def on_increase():
    sel = order_listbox.curselection()
    if not sel:
        messagebox.showinfo("Info", "Select an item first.")
        return
    name = order_listbox.get(sel[0]).split(" x ")[0]
    for iid, v in order.items():
        if v["item"]["name"] == name:
            v["quantity"] += 1
            break
    refresh_order_panel()

def on_decrease():
    sel = order_listbox.curselection()
    if not sel:
        messagebox.showinfo("Info", "Select an item first.")
        return
    name = order_listbox.get(sel[0]).split(" x ")[0]
    for iid, v in list(order.items()):
        if v["item"]["name"] == name:
            v["quantity"] -= 1
            if v["quantity"] <= 0:
                del order[iid]
            break
    refresh_order_panel()

def remove_item_by_selection():
    sel = order_listbox.curselection()
    if not sel:
        messagebox.showinfo("Info", "Select an item first.")
        return
    name = order_listbox.get(sel[0]).split(" x ")[0]
    for iid, v in list(order.items()):
        if v["item"]["name"] == name:
            del order[iid]
            break
    refresh_order_panel()

tk.Button(controls, text="+", width=3, command=on_increase).pack(side="left", padx=5)
tk.Button(controls, text="-", width=3, command=on_decrease).pack(side="left", padx=5)
tk.Button(controls, text="Remove", command=remove_item_by_selection).pack(side="left", padx=10)

total_label = tk.Label(order_panel, text="Total: 0",
                       font=("Helvetica", 12, "bold"), bg="#f8f8f8")
total_label.pack(pady=10)

tk.Button(order_panel, text="Checkout", bg="black", fg="white",
          width=20, command=on_checkout).pack(pady=20)

# -------------------------------------------------
# Bind & Run
# -------------------------------------------------

def on_canvas_configure(event):
    menu_canvas.configure(scrollregion=menu_canvas.bbox("all"))

menu_inner.bind("<Configure>", on_canvas_configure)

def on_root_resize(event):
    rebuild_menu_grid()

root.bind("<Configure>", on_root_resize)

root.after(150, rebuild_menu_grid)
root.mainloop()
