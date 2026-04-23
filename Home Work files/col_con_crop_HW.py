import cv2
import matplotlib.pyplot as plt

image_rgb = cv2.imread(r"C:\AI and ML new program 2026\Class Work files\image_Manipulation\website.jpg")
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

cropped_image = image_rgb[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()