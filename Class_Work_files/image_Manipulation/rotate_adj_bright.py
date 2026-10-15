import cv2
import numpy as np
import matplotlib.pyplot as plt

image_rgb = cv2.imread(r"C:\AI and ML new program 2026\Class Work files\image_Manipulation\website.jpg")

image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

(h, w) = image_rgb.shape[:2]
center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image_rgb, M, (w, h))

rotated_image = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_image)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(rotated_image.shape, dtype="uint8") * 50
brightened_image = cv2.add(rotated_image, brightness_matrix)

brighter_rgb = cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brightened Image")
plt.show()