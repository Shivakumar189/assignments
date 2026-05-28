# Assignment: Image as Numbers (06/04/2026)
# Load an image, print shape, pixel values, channels, and explain them

import numpy as np
import matplotlib.pyplot as plt

print("=" * 55)
print("     🖼️  Image as Numbers — Pixel Analysis")
print("=" * 55)

# ── Create a synthetic 6x6 RGB image ──────────────
# (In real assignment, use: img = cv2.imread('image.jpg') or PIL)
np.random.seed(7)
img = np.zeros((6, 6, 3), dtype=np.uint8)

# Add color regions
img[0:2, :] = [255, 0, 0]     # Red region (top)
img[2:4, :] = [0, 255, 0]     # Green region (middle)
img[4:6, :] = [0, 0, 255]     # Blue region (bottom)
img[:, 3:] += np.random.randint(0, 50, (6, 3, 3), dtype=np.uint8)  # slight noise

print(f"\n📐 Image Shape : {img.shape}")
print(f"   → {img.shape[0]} rows (Height)")
print(f"   → {img.shape[1]} columns (Width)")
print(f"   → {img.shape[2]} channels (RGB)")
print(f"\n📊 Total Pixels: {img.shape[0] * img.shape[1]}")
print(f"📦 Data Type   : {img.dtype}")
print(f"🔢 Value Range : 0 to 255 (8-bit per channel)")

print("\n🔴 Red Channel (pixel values):")
print(img[:, :, 0])

print("\n🟢 Green Channel (pixel values):")
print(img[:, :, 1])

print("\n🔵 Blue Channel (pixel values):")
print(img[:, :, 2])

# ── Visualize ─────────────────────────────────────
fig, axes = plt.subplots(1, 4, figsize=(12, 4))
titles = ['Original (RGB)', 'Red Channel', 'Green Channel', 'Blue Channel']
cmaps  = [None, 'Reds', 'Greens', 'Blues']
data   = [img, img[:,:,0], img[:,:,1], img[:,:,2]]

for ax, d, title, cmap in zip(axes, data, titles, cmaps):
    ax.imshow(d, cmap=cmap)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.axis('off')

plt.suptitle('Image as Numbers — RGB Channel Breakdown', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('16_image_as_numbers.png', dpi=150)
plt.show()
print("\n✅ Saved as '16_image_as_numbers.png'")

print("""
📝 Explanation:
  • Every image is a 3D NumPy array: (Height × Width × Channels)
  • Each pixel has 3 values (R, G, B), each between 0–255
  • 0 = no color, 255 = maximum intensity of that color
  • A grayscale image has shape (H, W) — only 1 channel
  • OpenCV loads images as BGR; Matplotlib displays in RGB
""")
