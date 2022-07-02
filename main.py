import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow("Cam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()