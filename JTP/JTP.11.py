import cv2
import time
import pyautogui
import mediapipe as mp

# -------------------------
# MediaPipe Setup
# -------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# -------------------------
# Settings
# -------------------------
SCROLL_SPEED = 250
SCROLL_DELAY = 0.4

CAM_WIDTH = 640
CAM_HEIGHT = 480

last_scroll_time = 0


def detect_gesture(hand_landmarks, handedness):
    """
    Open Palm  -> Scroll Up
    Closed Fist -> Scroll Down
    """

    lm = hand_landmarks.landmark

    fingers = []

    # Index
    fingers.append(
        lm[mp_hands.HandLandmark.INDEX_FINGER_TIP].y <
        lm[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    )

    # Middle
    fingers.append(
        lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y <
        lm[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    )

    # Ring
    fingers.append(
        lm[mp_hands.HandLandmark.RING_FINGER_TIP].y <
        lm[mp_hands.HandLandmark.RING_FINGER_PIP].y
    )

    # Pinky
    fingers.append(
        lm[mp_hands.HandLandmark.PINKY_TIP].y <
        lm[mp_hands.HandLandmark.PINKY_PIP].y
    )

    # Thumb
    thumb_tip = lm[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = lm[mp_hands.HandLandmark.THUMB_IP]

    if handedness == "Right":
        fingers.append(thumb_tip.x > thumb_ip.x)
    else:
        fingers.append(thumb_tip.x < thumb_ip.x)

    total = sum(fingers)

    if total == 5:
        return "scroll_up"

    elif total == 0:
        return "scroll_down"

    return "none"


# -------------------------
# Camera Setup
# -------------------------
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

prev_time = 0

print("\nGesture Scroll Control Started")
print("✋ Open Palm  → Scroll Up")
print("✊ Closed Fist → Scroll Down")
print("Press 'q' to quit\n")

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        continue

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks, hand_info in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            gesture = detect_gesture(
                hand_landmarks,
                hand_info.classification[0].label
            )

            current_time = time.time()

            if (
                gesture != "none"
                and current_time - last_scroll_time > SCROLL_DELAY
            ):

                if gesture == "scroll_up":
                    pyautogui.scroll(SCROLL_SPEED)

                elif gesture == "scroll_down":
                    pyautogui.scroll(-SCROLL_SPEED)

                last_scroll_time = current_time

            cv2.putText(
                frame,
                gesture.upper(),
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    # FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Mac Gesture Scroll Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()