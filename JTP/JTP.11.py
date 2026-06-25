import cv2
import mediapipe as mp
import numpy as np
import time

# -----------------------------
# MediaPipe Setup
# -----------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

mp_draw = mp.solutions.drawing_utils

# -----------------------------
# Camera Setup
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# -----------------------------
# Filter Settings
# -----------------------------
current_filter = "NORMAL"

THRESHOLD = 0.05
GESTURE_DELAY = 1.0  # seconds
last_gesture_time = 0

# -----------------------------
# Filter Function
# -----------------------------
def apply_filter(frame, filter_name):

    if filter_name == "GRAYSCALE":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    elif filter_name == "SEPIA":
        kernel = np.array([
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131]
        ])

        sepia = cv2.transform(frame, kernel)
        sepia = np.clip(sepia, 0, 255)
        return sepia.astype(np.uint8)

    elif filter_name == "NEGATIVE":
        return cv2.bitwise_not(frame)

    elif filter_name == "BLUR":
        return cv2.GaussianBlur(frame, (15, 15), 0)

    return frame


# -----------------------------
# Main Loop
# -----------------------------
while True:

    success, frame = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            thumb = hand_landmarks.landmark[
                mp_hands.HandLandmark.THUMB_TIP
            ]

            index = hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP
            ]

            middle = hand_landmarks.landmark[
                mp_hands.HandLandmark.MIDDLE_FINGER_TIP
            ]

            ring = hand_landmarks.landmark[
                mp_hands.HandLandmark.RING_FINGER_TIP
            ]

            pinky = hand_landmarks.landmark[
                mp_hands.HandLandmark.PINKY_TIP
            ]

            # Distances
            d_index = np.hypot(
                thumb.x - index.x,
                thumb.y - index.y
            )

            d_middle = np.hypot(
                thumb.x - middle.x,
                thumb.y - middle.y
            )

            d_ring = np.hypot(
                thumb.x - ring.x,
                thumb.y - ring.y
            )

            d_pinky = np.hypot(
                thumb.x - pinky.x,
                thumb.y - pinky.y
            )

            current_time = time.time()

            if current_time - last_gesture_time > GESTURE_DELAY:

                if d_index < THRESHOLD:
                    current_filter = "GRAYSCALE"
                    last_gesture_time = current_time
                    print("Filter: GRAYSCALE")

                elif d_middle < THRESHOLD:
                    current_filter = "SEPIA"
                    last_gesture_time = current_time
                    print("Filter: SEPIA")

                elif d_ring < THRESHOLD:
                    current_filter = "NEGATIVE"
                    last_gesture_time = current_time
                    print("Filter: NEGATIVE")

                elif d_pinky < THRESHOLD:
                    current_filter = "BLUR"
                    last_gesture_time = current_time
                    print("Filter: BLUR")

    # Apply currently selected filter
    filtered_frame = apply_filter(frame.copy(), current_filter)

    # Display current filter
    cv2.putText(
        filtered_frame,
        f"Filter: {current_filter}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        filtered_frame,
        "Index=Gray | Middle=Sepia | Ring=Negative | Pinky=Blur",
        (10, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        filtered_frame,
        "Press C to Capture | Q to Quit",
        (10, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("Gesture Controlled Camera", filtered_frame)

    key = cv2.waitKey(1) & 0xFF

    # Capture image with current filter
    if key == ord('c'):
        filename = f"captured_{time.strftime('%Y%m%d-%H%M%S')}.jpg"
        cv2.imwrite(filename, filtered_frame)
        print(f"Photo saved: {filename}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()