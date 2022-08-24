from turtle import distance
import cv2
from handtracking import HandDetector

cam = cv2.VideoCapture(0)
handler = HandDetector()

while True:
    ret, frame = cam.read()
    cv2.imshow("Cam", frame)

    handsPoints = handler.getPoint((4,8), frame)

    if handsPoints:
        indexFingerPoint = handsPoints[0][0]
        thumbFingerPoint = handsPoints[0][1]
        distanceBetweenFingers = abs(indexFingerPoint[0]-thumbFingerPoint[0]) + abs(indexFingerPoint[1]-thumbFingerPoint[1])
        if distanceBetweenFingers < 100:
            print("Thank you, GoodBye.")
            break


    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()