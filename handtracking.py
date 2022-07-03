import cv2
import mediapipe as mp

handsMp = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = handsMp.Hands()


def getPoint(point, image):
    h, w, c = image.shape

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            pointxy = hand_landmarks.landmark[point]
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