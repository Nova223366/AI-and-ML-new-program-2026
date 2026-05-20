import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        return

    mode = 'n'
    brightness_level = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape

        if mode == 'n':
            processed_frame = frame
            cv2.putText(processed_frame, "Normal View", (20, 40), 
                        cv2.FONT_HERSHEY_SHORT_DATA_GENESIS, 0.7, (0, 255, 0), 1)

        elif mode == 'r':
            processed_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            cv2.putText(processed_frame, "Rotated 90", (20, 40), 
                        cv2.FONT_HERSHEY_SHORT_DATA_GENESIS, 0.7, (0, 255, 0), 1)

        elif mode == 'c':
            start_x, start_y = int(w * 0.25), int(h * 0.25)
            end_x, end_y = int(w * 0.75), int(h * 0.75)
            cropped = frame[start_y:end_y, start_x:end_x]
            processed_frame = cv2.resize(cropped, (w, h))
            cv2.putText(processed_frame, "Cropped & Zoomed", (20, 40), 
                        cv2.FONT_HERSHEY_SHORT_DATA_GENESIS, 0.7, (0, 255, 0), 1)

        elif mode == 'b':
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            v_channel = hsv[:, :, 2]
            
            if brightness_level > 0:
                v_channel = np.where(v_channel <= 255 - brightness_level, v_channel + brightness_level, 255)
            elif brightness_level < 0:
                v_channel = np.where(v_channel >= abs(brightness_level), v_channel + brightness_level, 0)
                
            hsv[:, :, 2] = v_channel
            processed_frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            cv2.putText(processed_frame, f"Brightness: {brightness_level}", (20, 40), 
                        cv2.FONT_HERSHEY_SHORT_DATA_GENESIS, 0.7, (0, 255, 0), 1)

        cv2.imshow("Manipulation Window", processed_frame)

        key = cv2.waitKey(1) & 0xFF
        
        if key in [ord('n'), ord('r'), ord('c'), ord('b')]:
            mode = chr(key)
        elif key == ord('u') and mode == 'b':
            brightness_level = min(brightness_level + 20, 100)
        elif key == ord('d') and mode == 'b':
            brightness_level = max(brightness_level - 20, -100)
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
