import cv2
import mediapipe as mp


class HandDetector():
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()

    def getPoint(self, handPoint, image):
        h, w, _ = image.shape

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)

        if not results.multi_hand_landmarks:
            return None

        elif len(results.multi_hand_landmarks) == 1:
            hand_landmarks = results.multi_hand_landmarks[0]
            pointxy = hand_landmarks.landmark[handPoint]
            cx, cy = int(pointxy.x*w), int(pointxy.y*h)
            return (cx, cy)
        else:
            multiHandsPoints = []
            for hand_landmarks in results.multi_hand_landmarks:
                pointxy = hand_landmarks.landmark[handPoint]
                cx, cy = int(pointxy.x*w), int(pointxy.y*h)
                multiHandsPoints.append((cx, cy))
            return multiHandsPoints
        




def main():

    cap = cv2.VideoCapture(0)
    hd = HandDetector()
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        points = hd.getPoint(8, image)
        print(points)

            # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()

if __name__ == "__main__":
    main()