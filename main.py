import cv2

cap = cv2.VideoCapture(2)

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Capturing...', frame)
    else:
        break

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
