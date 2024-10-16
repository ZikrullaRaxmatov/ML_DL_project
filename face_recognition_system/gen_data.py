import cv2
import os

cap = cv2.VideoCapture(2)

'''
try:
    if os.path.exists('../face_recognition_system/generated_data'):
        os.mkdir('../face_recognition_system/generated_data')
except OSError:
    print('Error: Creating directory of data')
'''

currentFrame = 0

while True:
    
    ret, frame = cap.read()
    

    if ret:
        name = 'frame' + str(currentFrame) + '.jpg'

        print('Creating... ' + name)

        cv2.imwrite(f'./generated_data/{name}', frame)

        currentFrame += 1
    
    else:
        break

    cv2.imshow('Showing ...', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()