import cv2
import mediapipe as mp
from mediapipe.mp.solutions.hands import Hands


class HandDetector():
    def __init__(self):
        self.hands = Hands()

    def getPoint(self, handPoint, image):
        h, w, _ = image.shape

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image)

        for hand_landmarks in results.multi_hand_landmarks:
            pointxy = hand_landmarks.landmark[handPoint]
            cx, cy = int(pointxy.x*w), int(pointxy.y*h)
            print(cx, cy)


def main():

    cap = cv2.VideoCapture(0)
    with handsMp.Hands() as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            getPoint(0, image)

                # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if cv2.waitKey(1) & 0xFF == 27:
                    break
    cap.release()

if __name__ == "__main__":
    main()