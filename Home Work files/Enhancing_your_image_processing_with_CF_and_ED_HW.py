import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        return

    mode = 'r'

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if mode == 'r':
            processed_frame = frame
            cv2.putText(processed_frame, "Normal Mode", (15, 35), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)

        elif mode == 'g':
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            processed_frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            cv2.putText(processed_frame, "Grayscale Mode", (15, 35), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)

        elif mode == 'c':
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            canny = cv2.Canny(blurred, 60, 120)
            processed_frame = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
            cv2.putText(processed_frame, "Canny Edges", (15, 35), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)

        elif mode == 's':
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (3, 3), 0)
            sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
            combined = np.sqrt(sobel_x**2 + sobel_y**2)
            sobel_output = np.uint8(combined)
            processed_frame = cv2.cvtColor(sobel_output, cv2.COLOR_GRAY2BGR)
            cv2.putText(processed_frame, "Sobel Edges", (15, 35), 
                        cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)

        cv2.imshow("Workspace", processed_frame)

        key = cv2.waitKey(1) & 0xFF
        if key in [ord('r'), ord('g'), ord('h'), ord('c'), ord('s')]:
            mode = chr(key)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
