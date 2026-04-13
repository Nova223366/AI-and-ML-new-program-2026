import cv2

image = cv2.imread(r"C:\AI and ML new program 2026\Class Work files\Computer vision\website.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (224, 224))

cv2.imshow("Processed Image", resized_image)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite(r"C:\AI and ML new program 2026\Class Work files\Computer vision\processed_image.jpg", resized_image)
    print("Image saved successfully.")

else:
    print("Image not saved.")

cv2.destroyAllWindows()

print(f"Processed Image Dimensions: {resized_image.shape}")