import cv2, time, pyautogui 
import mediapipe as mp  

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.7)
mp_drawing = mp.solutions.drawing_utils

SCROLL_SPEED = 300
SCROLL_DELAY = 0.1
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.THUMB_TIP]
    
    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or (handedness == "Left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1)

    return "scroll_up" if sum(fingers) == 5 else "scroll_down" if sum(fingers) == 0 else "none"

cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)
last__scroll = p_time = 0
print("Gesture Scroll control active\nOpen palm: Scroll up\nFirst: Scroll down\npress 'q' to quit")

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks, hand_handedness.classification[0].label)
            current_time = time.time()
            if gesture != "none" and current_time - last__scroll > SCROLL_DELAY:
                pyautogui.scroll(SCROLL_SPEED if gesture == "scroll_up" else -SCROLL_SPEED)
                last__scroll = current_time

    c_time = time.time()
    fps = 1 / (c_time - p_time) if c_time != p_time else 0
    p_time = c_time
    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Gesture Scroll Control", img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()