"""
Generate the Open Graph social-share image for reliquery.app.

Output: public/og.png (1200x630)
Run from project root: python scripts/generate-og.py
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W, H = 1200, 630

# Brand colors
PURPLE = (64, 5, 63)        # #40053f
PURPLE_LIGHT = (122, 28, 120)  # #7a1c78
ORANGE = (242, 103, 9)       # #f26709
ORANGE_DEEP = (161, 65, 4)   # #a14104

# Diagonal gradient: top-left purple → bottom-right orange
img = Image.new("RGB", (W, H), PURPLE)
draw = ImageDraw.Draw(img)

# Build gradient pixel-by-pixel using diagonal interpolation
for y in range(H):
    for x in range(W):
        # Diagonal progress 0..1
        t = (x / W * 0.7) + (y / H * 0.3)
        # Curve it slightly so purple dominates
        t = max(0, min(1, t * 1.2 - 0.1))
        r = int(PURPLE[0] + (ORANGE[0] - PURPLE[0]) * t)
        g = int(PURPLE[1] + (ORANGE[1] - PURPLE[1]) * t)
        b = int(PURPLE[2] + (ORANGE[2] - PURPLE[2]) * t)
        img.putpixel((x, y), (r, g, b))

# Add radial glow blobs (stained glass tint feel)
glow = Image.new("RGB", (W, H), (0, 0, 0))
glow_draw = ImageDraw.Draw(glow)
# Orange highlight bottom-right
glow_draw.ellipse((W * 0.55, H * 0.45, W * 1.05, H * 1.1),
                  fill=(255, 140, 40))
# Purple deeper top-left
glow_draw.ellipse((-W * 0.1, -H * 0.2, W * 0.5, H * 0.7),
                  fill=(60, 0, 60))
glow = glow.filter(ImageFilter.GaussianBlur(radius=200))
img = Image.blend(img, glow, 0.35)

# Stained glass octagonal pattern overlay
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)
size = 90
for ox in range(0, W + size, size):
    for oy in range(0, H + size, size):
        # Octagon points (clockwise from top-left chamfer)
        c = size * 0.29
        pts = [
            (ox + c, oy),
            (ox + size - c, oy),
            (ox + size, oy + c),
            (ox + size, oy + size - c),
            (ox + size - c, oy + size),
            (ox + c, oy + size),
            (ox, oy + size - c),
            (ox, oy + c),
        ]
        overlay_draw.polygon(pts, outline=(255, 255, 255, 22), width=1)

img = Image.alpha_composite(img.convert("RGBA"), overlay)
# Stay on RGBA so alpha-blended chip + text composite correctly
draw = ImageDraw.Draw(img)

# Fonts
font_dir = "C:/Windows/Fonts"
serif_bold = ImageFont.truetype(os.path.join(font_dir, "georgiab.ttf"), 132)
serif_reg = ImageFont.truetype(os.path.join(font_dir, "georgia.ttf"), 38)
sans_small = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 22)
sans_tag = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 18)

# Top-left: small chip
chip_text = "CHROME EXTENSION"
chip_bbox = draw.textbbox((0, 0), chip_text, font=sans_tag)
chip_w = chip_bbox[2] - chip_bbox[0]
chip_pad_x, chip_pad_y = 18, 9
chip_x, chip_y = 80, 80
draw.rounded_rectangle(
    (chip_x, chip_y, chip_x + chip_w + chip_pad_x * 2, chip_y + 36),
    radius=18,
    fill=(0, 0, 0, 90),
    outline=(255, 255, 255, 130),
    width=1,
)
draw.text((chip_x + chip_pad_x, chip_y + chip_pad_y - 2), chip_text,
          font=sans_tag, fill=(255, 255, 255, 255))

# Centered wordmark
title = "Reliquery"
tbbox = draw.textbbox((0, 0), title, font=serif_bold)
tw = tbbox[2] - tbbox[0]
th = tbbox[3] - tbbox[1]
tx = (W - tw) // 2
ty = (H - th) // 2 - 70
draw.text((tx, ty), title, font=serif_bold, fill=(255, 255, 255))

# Tagline below the wordmark
tagline_l1 = "Your brand's most valuable artifacts."
tagline_l2 = "At work on every page."
for i, line in enumerate([tagline_l1, tagline_l2]):
    bbox = draw.textbbox((0, 0), line, font=serif_reg)
    lw = bbox[2] - bbox[0]
    color = (255, 255, 255, 240) if i == 0 else (255, 200, 140, 255)  # second line orange-tinted
    draw.text(((W - lw) // 2, ty + th + 50 + i * 52), line, font=serif_reg, fill=color)

# Bottom-right: URL
url = "reliquery.app"
ubbox = draw.textbbox((0, 0), url, font=sans_small)
uw = ubbox[2] - ubbox[0]
draw.text((W - uw - 80, H - 60), url, font=sans_small,
          fill=(255, 255, 255, 200))

# Save (flatten to RGB for smaller file size — JPEG-friendly if we ever want)
os.makedirs("public", exist_ok=True)
img.convert("RGB").save("public/og.png", optimize=True)
print(f"Saved public/og.png ({W}x{H})")
