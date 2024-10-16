import cv2
import os

cap = cv2.VideoCapture(2)

try:
    if os.path.exists('./generated_data'):
        os.mkdir('./generated_data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0

while True:
    
    ret, frame = cap.read()
    
    cv2.imshow('Showing ...', frame)

    if ret:
        name = './generated_data/frame' + str(currentFrame) + '.jpg'

        print('Creating... ' + name)

        cv2.imwrite(name, frame)

        currentFrame += 1
    
    else:
        break

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()