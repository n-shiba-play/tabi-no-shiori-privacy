"""Make help images from existing, fictional-data Simulator captures.

Only crops and resizes real app screenshots. No UI text or controls are edited.
Requires Pillow; run from any directory with `python prepare_images.py`.
"""

import os
from pathlib import Path

from PIL import Image, ImageOps


REPOSITORY = Path(__file__).resolve().parents[2]
SOURCE = REPOSITORY / "AppStoreAssets" / "raw"
OUTPUT = Path(
    os.environ.get("SHIORING_SUPPORT_OUTPUT_ROOT", REPOSITORY / "support" / "assets" / "images")
)
OUTPUT.mkdir(parents=True, exist_ok=True)

CAPTURES = {
    "help-cover.jpg": ("01_cover.png", (0, 180, 1320, 2500)),
    "help-itinerary.jpg": ("04_transport_day1_full.png", (0, 360, 1320, 2430)),
    "help-map.jpg": ("03_map.png", (0, 180, 1320, 2810)),
    "help-packing.jpg": ("05_packing.png", (0, 910, 1320, 2650)),
    "help-budget.jpg": ("05_budget.png", (0, 360, 1320, 2660)),
    "help-pdf.jpg": ("06_pdf_preview.png", (0, 170, 1320, 2670)),
}

for name, (source_name, crop) in CAPTURES.items():
    with Image.open(SOURCE / source_name) as original:
        image = ImageOps.exif_transpose(original).convert("RGB").crop(crop)
        height = round(image.height * 960 / image.width)
        image = image.resize((960, height), Image.Resampling.LANCZOS)
        image.save(OUTPUT / name, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"{name}: {image.width} x {image.height}")
