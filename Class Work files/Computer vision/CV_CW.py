import cv2

image = cv2.imread(r"C:\AI and ML new program 2026\Class Work files\Computer vision\website.jpg")

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image", 800, 500)

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"image Dimensions: {image.shape}")