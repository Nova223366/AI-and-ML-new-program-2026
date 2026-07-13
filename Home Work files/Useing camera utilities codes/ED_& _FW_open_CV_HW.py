import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_edge_detection(image, method="sobel", ksize=3, threshold1=100, threshold2=200):
    if method == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
        return cv2.convertScaleAbs(sobelx) | cv2.convertScaleAbs(sobely)

    elif method == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, threshold1, threshold2)

    elif method == "laplacian":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lap = cv2.Laplacian(gray, cv2.CV_64F)
        return cv2.convertScaleAbs(lap)

def apply_filter(image, filter_type="gaussian", ksize=5):
    if filter_type == "gaussian":
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    elif filter_type == "median":
        return cv2.medianBlur(image, ksize)

def interactive_edge_detection():
    # ✅ clean input properly
    image_path = input("Enter image path: ").strip()
    image_path = image_path.replace("\\", "/").replace('"', '')

    print("Loading:", image_path)  # debug

    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found. Check path carefully.")
        return

    print("✅ Image loaded successfully!")

    while True:
        print("\nSelect an option:")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Apply Gaussian Filter")
        print("5. Apply Median Filter")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            ksize = int(input("Kernel size (3,5,7): "))
            result = apply_edge_detection(image, "sobel", ksize=ksize)
            display_image("Sobel", result)

        elif choice == '2':
            t1 = int(input("Lower threshold: "))
            t2 = int(input("Upper threshold: "))
            result = apply_edge_detection(image, "canny", threshold1=t1, threshold2=t2)
            display_image("Canny", result)

        elif choice == '3':
            result = apply_edge_detection(image, "laplacian")
            display_image("Laplacian", result)

        elif choice == '4':
            result = apply_filter(image, "gaussian")
            display_image("Gaussian Blur", result)

        elif choice == '5':
            result = apply_filter(image, "median")
            display_image("Median Blur", result)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

# ✅ run program
interactive_edge_detection()