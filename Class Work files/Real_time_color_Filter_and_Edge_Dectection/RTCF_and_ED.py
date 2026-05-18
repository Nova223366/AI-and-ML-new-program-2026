import cv2
import numpy as np

def apply_filter(image, ftype):
    img = image.copy()
    if ftype == "red_tint":
        img[:, :, 1] = img[:, :, 0] = 0

    elif ftype == "green_tint":
        img[:, :, 0] = img[:, :, 2] = 0

    elif ftype == "blue_tint":
        img[:, :, 1] = img[:, :, 2] = 0

    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        SX = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = 3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = 3)
        sob = cv2.bitwise_or(SX.astype(np.uint8), sy.astype(np.uint8))
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)

    elif ftype == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

    elif ftype == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, 9, 250, 250)
        img = cv2.bitwise_and(color, color, mask=edges)

    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return
    ftype = "original"
    print("Press 'r' for red tint, 'g' for green tint, 'b' for blue tint, 's' for sobel, 'c' for canny, 't' for cartoon, and 'o' for original.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        filtered_frame = apply_filter(frame, ftype)
        cv2.imshow('Real-Time Filter and Edge Detection', filtered_frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            ftype = "red_tint"
        elif key == ord('g'):
            ftype = "green_tint"
        elif key == ord('b'):
            ftype = "blue_tint"
        elif key == ord('s'):
            ftype = "sobel"
        elif key == ord('c'):
            ftype = "canny"
        elif key == ord('t'):
            ftype = "cartoon"
        elif key == ord('o'):
            ftype = "original"

    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()