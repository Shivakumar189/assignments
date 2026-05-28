# Assignment: Image Filter Lab (08/04/2026)
# Use OpenCV to grayscale, blur, detect edges and show before/after

import cv2
import numpy as np
import matplotlib.pyplot as plt

print("=" * 55)
print("     🧪 Image Filter Lab — OpenCV")
print("=" * 55)

# ── Create a test image (replaces real image load) ─
# In real use: img = cv2.imread('photo.jpg')
img_rgb = np.zeros((200, 300, 3), dtype=np.uint8)
cv2.rectangle(img_rgb, (30,  30), (130, 130), (220, 60, 60),  -1)  # Red square
cv2.rectangle(img_rgb, (150, 30), (270, 130), (60, 180, 60),  -1)  # Green square
cv2.circle(img_rgb, (150, 160), 35, (60, 60, 220), -1)              # Blue circle
cv2.putText(img_rgb, "OpenCV", (70, 185), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (255, 255, 255), 2)

# OpenCV uses BGR internally
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

# ── 1. Grayscale ──────────────────────────────────
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
print("✅ Grayscale conversion done.")

# ── 2. Gaussian Blur ──────────────────────────────
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
print("✅ Gaussian blur applied (kernel 11×11).")

# ── 3. Edge Detection (Canny) ─────────────────────
edges = cv2.Canny(blurred, threshold1=30, threshold2=100)
print("✅ Canny edge detection applied.")

# ── Plot: Before & After ──────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
fig.suptitle('Image Filter Lab — Before & After', fontsize=14, fontweight='bold')

axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title('Original (Color)', fontsize=11)

axes[0, 1].imshow(gray, cmap='gray')
axes[0, 1].set_title('Grayscale', fontsize=11)

axes[1, 0].imshow(blurred, cmap='gray')
axes[1, 0].set_title('Gaussian Blur', fontsize=11)

axes[1, 1].imshow(edges, cmap='gray')
axes[1, 1].set_title('Canny Edge Detection', fontsize=11)

for ax in axes.flat:
    ax.axis('off')

plt.tight_layout()
plt.savefig('17_image_filter_lab.png', dpi=150)
plt.show()
print("\n✅ Saved as '17_image_filter_lab.png'")

print("""
📝 Filter Explanations:
  🔲 Grayscale   : Converts 3-channel (R,G,B) image to 1-channel by
                   averaging color intensities. Reduces computation.

  🌊 Gaussian Blur: Smooths the image by averaging each pixel with
                   its neighbors using a weighted kernel. Reduces noise.

  ✏️  Canny Edges : Detects abrupt changes in intensity (edges) by
                   computing image gradients. Uses two thresholds to
                   keep only strong, connected edges.
""")
