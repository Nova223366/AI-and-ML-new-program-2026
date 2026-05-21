import cv2
import mediapipe as mp
import numpy as np
import time

# -------------------------------
# Initialize MediaPipe Hands
# -------------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# -------------------------------
# Webcam
# -------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access webcam")
    exit()

# -------------------------------
# FPS Variables
# -------------------------------
prev_time = 0

# -------------------------------
# Modes
# -------------------------------
mode = "NORMAL"

# -------------------------------
# Finger Detection Function
# -------------------------------
def count_fingers(hand_landmarks):

    tips = [4, 8, 12, 16, 20]

    fingers = []

    # Thumb
    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

# -------------------------------
# Main Loop
# -------------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    h, w, c = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    processed_frame = frame.copy()

    finger_count = 0

    # -------------------------------
    # Hand Detection
    # -------------------------------
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                processed_frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Count fingers
            finger_count = count_fingers(hand_landmarks)

            # ---------------------------------
            # Gesture Controls
            # ---------------------------------
            if finger_count == 0:
                mode = "BLUR"

            elif finger_count == 1:
                mode = "GRAYSCALE"

            elif finger_count == 2:
                mode = "CANNY"

            elif finger_count == 3:
                mode = "SOBEL"

            elif finger_count == 4:
                mode = "CARTOON"

            elif finger_count == 5:
                mode = "NORMAL"

    # -------------------------------
    # Apply Modes
    # -------------------------------

    if mode == "GRAYSCALE":

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        processed_frame = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )

    elif mode == "CANNY":

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blur, 60, 120)

        processed_frame = cv2.cvtColor(
            edges,
            cv2.COLOR_GRAY2BGR
        )

    elif mode == "SOBEL":

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

        sobel = np.sqrt(sobelx**2 + sobely**2)

        sobel = np.uint8(np.clip(sobel, 0, 255))

        processed_frame = cv2.cvtColor(
            sobel,
            cv2.COLOR_GRAY2BGR
        )

    elif mode == "BLUR":

        processed_frame = cv2.GaussianBlur(
            frame,
            (35, 35),
            0
        )

    elif mode == "CARTOON":

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray = cv2.medianBlur(gray, 5)

        edges = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            9,
            9
        )

        color = cv2.bilateralFilter(frame, 9, 300, 300)

        processed_frame = cv2.bitwise_and(
            color,
            color,
            mask=edges
        )

    # -------------------------------
    # FPS Counter
    # -------------------------------
    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    # -------------------------------
    # Display Information
    # -------------------------------
    cv2.putText(
        processed_frame,
        f"Mode: {mode}",
        (15, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        processed_frame,
        f"Fingers: {finger_count}",
        (15, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.putText(
        processed_frame,
        f"FPS: {int(fps)}",
        (15, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # -------------------------------
    # Gesture Instructions
    # -------------------------------
    cv2.putText(
        processed_frame,
        "0=Blur 1=Gray 2=Canny 3=Sobel 4=Cartoon 5=Normal",
        (15, h - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # -------------------------------
    # Show Output
    # -------------------------------
    cv2.imshow("Gesture Control Vision System", processed_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# -------------------------------
# Cleanup
# -------------------------------
cap.release()
cv2.destroyAllWindows()