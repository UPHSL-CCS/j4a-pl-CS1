# check_assets.py
import os

# Import menu_items without needing a package
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

from menu import menu_items  # now works

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
required_images = ["logo.png", "placeholder.png"]

for category, items in menu_items.items():
    for item in items:
        if "image" in item and item["image"]:
            required_images.append(item["image"])
        else:
            name_file = item["name"].lower().replace(" ", "_") + ".png"
            required_images.append(name_file)

missing = []
for img in required_images:
    path = os.path.join(ASSETS_DIR, img)
    if not os.path.exists(path):
        missing.append(img)

if missing:
    print("Missing image files:")
    for m in missing:
        print("-", m)
else:
    print("All images exist.")
