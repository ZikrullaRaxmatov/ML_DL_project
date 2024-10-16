import cv2
import os

cap = cv2.VideoCapture(2)

try:
    if os.path.exists('gen_data'):
        os.mkdir('gen_data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0

while True:
    '''
    ret, frame = cap.read()

    if ret:
        name = './gen_data/frame' + currentFrame + '.jpg'

        print('Creating... ' + name)

        cv2.imwrite(name, frame)

        currentFrame += 1
    
    else:
        break
    '''

    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()