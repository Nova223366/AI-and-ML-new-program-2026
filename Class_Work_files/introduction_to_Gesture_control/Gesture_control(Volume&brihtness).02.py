import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from math import hypot
import screen_brightness_control as sbc

# Initialize MediaPipe Hands and Drawing Utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# --- FIXED PYCAW INITIALIZATION ---
try:
    # Use standard COM initialization to safely find the active speaker interface
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    min_vol, max_vol = volume.GetVolumeRange()[0:2]
except Exception as e:
    # Fallback method if standard GetSpeakers() properties throw errors
    try:
        from pycaw.pycaw import IMMDeviceEnumerator
        from comtypes import GUID
        
        CLSID_MMDeviceEnumerator = GUID('{BCDE0395-E52F-467C-8E3D-C4579291692E}')
        IMMDeviceEnumerator_iid = GUID('{A95664D2-9614-4F35-A746-DE8DB63617E6}')
        
        import comtypes.client
        enumerator = comtypes.client.CreateObject(CLSID_MMDeviceEnumerator, interface=IMMDeviceEnumerator)
        # 0 = eRender (playback), 0 = eConsole (default device role)
        speakers = enumerator.GetDefaultAudioEndpoint(0, 0) 
        interface = speakers.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        min_vol, max_vol = volume.GetVolumeRange()[0:2]
    except Exception as fallback_e:
        print(f"Pycaw initialization failed: {fallback_e}")
        exit()
# ----------------------------------

# Set up webcam capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.flip(img, 1)  # Mirror effect
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Retrieve frame dimensions for dynamic bar positioning
    h, w, _ = img.shape

    if results.multi_hand_landmarks and results.multi_handedness:
        for i, handLms in enumerate(results.multi_hand_landmarks):
            label = results.multi_handedness[i].classification[0].label  # "Left" or "Right"
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Get thumb and index finger tips
            thumb = handLms.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index = handLms.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_pos = (int(thumb.x * w), int(thumb.y * h))
            index_pos = (int(index.x * w), int(index.y * h))
            cv2.circle(img, thumb_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index_pos, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb_pos, index_pos, (0, 255, 0), 3)

            # Calculate the Euclidean distance between thumb and index finger
            dist = hypot(index_pos[0] - thumb_pos[0], index_pos[1] - thumb_pos[1])

            if label == "Right":  # Volume control with right hand
                vol = np.interp(dist, [30, 300], [min_vol, max_vol])
                try:
                    volume.SetMasterVolumeLevel(vol, None)
                except Exception as e:
                    print(f"Volume error: {e}")
                vol_bar = int(np.interp(dist, [30, 300], [400, 150]))
                cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
                cv2.rectangle(img, (50, vol_bar), (85, 400), (255, 0, 0), cv2.FILLED)
                vol_perc = int(np.interp(dist, [30, 300], [0, 100]))
                cv2.putText(img, f'{vol_perc}%', (40, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            elif label == "Left":  # Brightness control with left hand
                bright = np.interp(dist, [30, 300], [0, 100])
                try:
                    sbc.set_brightness(bright)
                except Exception as e:
                    print(f"Brightness error: {e}")
                bright_bar = int(np.interp(dist, [30, 300], [400, 150]))
                # Place brightness bar on the right end of the window
                x1, x2 = w - 85, w - 50
                cv2.rectangle(img, (x1, 150), (x2, 400), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, bright_bar), (x2, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(bright)}%', (w - 110, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
