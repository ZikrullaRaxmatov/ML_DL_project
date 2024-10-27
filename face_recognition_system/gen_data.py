import cv2
import os
import time

cap = cv2.VideoCapture(0)

try:
    if not os.path.exists('./datasets/generated_data'):
        os.mkdir('./datasets/generated_data')
except OSError:
    print('Error: Creating directory of data')


listSecond = []

while True:
    
    ret, frame = cap.read('../videos/men_1.mp4')

    if ret:
        
        currentSecond = str(time.time())
        listSecond = currentSecond.split('.')
        uniqueName = listSecond[0] + listSecond[1]

        name = 'frame' + str(uniqueName) + '.jpg'

        print('Creating... ' + name)

        cv2.imwrite(f'./datasets/generated_data/{name}', frame)

        cv2.imshow('Showing ...', frame)
    
    else:
        break


    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()