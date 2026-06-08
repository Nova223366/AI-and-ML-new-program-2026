import cv2, mediapipe as mp, time, numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

FILTERS = [None, 'GRAYSCALE', 'SEPIA', 'NEGATIVE', 'BLUR']
current_filter = 0

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

last_action_time = 0; DEBOUNCE_TIME = 1
pinch_in_progress = False; capture_in_progress = False

def apply_filter(frame, ftype):
    if ftype == 'GRAYSCALE':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif ftype == 'SEPIA':
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                 [0.349, 0.686, 0.168],
                                 [0.272, 0.534, 0.131]])
        return cv2.transform(frame, sepia_filter)
    elif ftype == 'NEGATIVE':
        return cv2.bitwise_not(frame)
    elif ftype == 'BLUR':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    else:
        return frame
    
while True:
    success, img = cap.read()
    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    img = cv2.flip(img, 1)
    h, w = img.shape[:2]
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    capture_request = False

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)

            if distance < 0.05 and not pinch_in_progress and time.time() - last_action_time > DEBOUNCE_TIME:
                pinch_in_progress = True
                last_action_time = time.time()
                current_filter = (current_filter + 1) % len(FILTERS)
                print(f"Filter changed to: {FILTERS[current_filter]}")

            if distance >= 0.05:
                pinch_in_progress = False

            if distance < 0.05 and not capture_in_progress and time.time() - last_action_time > DEBOUNCE_TIME:
                capture_in_progress = True
                last_action_time = time.time()
                capture_request = True

            if distance >= 0.05:
                capture_in_progress = False

            if results.multi_hand_landmarks and capture_request:
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                filename = f"captured_{timestamp}.jpg"
                cv2.imwrite(filename, img)
                print(f"Photo captured: {filename}")
    filtered_img = apply_filter(img, FILTERS[current_filter])
    cv2.imshow("Gesture Control Photo App", filtered_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
