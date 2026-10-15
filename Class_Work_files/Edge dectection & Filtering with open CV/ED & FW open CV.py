import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    # utility function to display image.
    plt.figure(figsize = (8, 8))
    if len(image.shape) == 2: # grayscale image
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_edge_dectection(image, method = "sobel", ksize = 3, threshold1 = 100, threshold2 = 200):
    if method == "sobel":
        # Apply Sobel edge detection
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=ksize)
        return cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
    elif method == "canny":
        # Apply Canny edge detection
        return cv2.Canny(image, threshold1, threshold2)
    elif method == "laplacian":
        return cv2.Laplacian(image, cv2.CV_64F).astype(np.uint8)

def apple_filter(image, filter_type = "gaussian", ksize = 5):
    if filter_type == "gaussian":
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    elif filter_type == "median":
        return cv2.medianBlur(image, ksize)
    
def interactive_edge_dectection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return
    print("Select an option: ")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Apply Gaussian Filter")   
    print("5. Apply Median Filter")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            ksize = int(input("Enter kernel size for Sobel (odd number, e.g., 3, 5, 7): "))
            result = apply_edge_dectection(image, method="sobel", ksize=ksize)
            display_image("Sobel Edge Detection", result)
        elif choice == '2':
            threshold1 = int(input("Enter lower threshold for Canny: "))
            threshold2 = int(input("Enter upper threshold for Canny: "))
            result = apply_edge_dectection(image, method="canny", threshold1=threshold1, threshold2=threshold2)
            display_image("Canny Edge Detection", result)
        elif choice == '3':
            edges = apply_edge_dectection(image, method="laplacian")
            display_image("Laplacian Edge Detection", edges)
        elif choice == '4':
            filtered_image = apple_filter(image, filter_type="gaussian")
            display_image("Gaussian Filtered Image", filtered_image)
        elif choice == '5':
            filtered_image = apple_filter(image, filter_type="median")
            display_image("Median Filtered Image", filtered_image)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


interactive_edge_dectection(r"C:\AI and ML new program 2026\Class Work files\Edge dectection & Filtering with open CV\website.jpg")