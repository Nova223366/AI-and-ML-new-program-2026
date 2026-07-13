import cv2
from deepface import DeepFace

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            predictions = DeepFace.analyze(
                img_path=frame, 
                actions=['emotion'], 
                enforce_detection=False,
                detector_backend='opencv'
            )
            
            for face in predictions:
                x = face['region']['x']
                y = face['region']['y']
                w = face['region']['w']
                h = face['region']['h']
                
                dominant_emotion = face['dominant_emotion']
                confidence = face['face_confidence']
                
                if confidence > 0.4:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    
                    label = f"{dominant_emotion.capitalize()}"
                    cv2.putText(frame, label, (x, y - 10), 
                                cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)
                                
        except Exception:
            pass

        cv2.imshow("Face & Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
