import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load image
# -------------------------------
image = cv2.imread(r"C:\AI and ML new program 2026\Class Work files\image_Manipulation\website.jpg")

if image is None:
    raise ValueError("Image not found. Check file path.")

# Convert BGR → RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# -------------------------------
# Step 2: Rotate image
# -------------------------------
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))

# Save rotated image
cv2.imwrite(r"C:\AI and ML new program 2026\Class Work files\image_Manipulation\rotated.jpg", rotated_image)

# Convert for display
rotated_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.axis("off")
plt.show()

# -------------------------------
# Step 3: Brighten image
# -------------------------------
brightness_matrix = np.ones(rotated_image.shape, dtype="uint8") * 50
brightened_image = cv2.add(rotated_image, brightness_matrix)

# Save brightened image
cv2.imwrite(r"C:\AI and ML new program 2026\Class Work files\image_Manipulation\brightened.jpg", brightened_image)

# Convert for display
bright_rgb = cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB)

plt.imshow(bright_rgb)
plt.title("Brightened Image")
plt.axis("off")
plt.show()