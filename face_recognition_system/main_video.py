from simple_facerec import SimpleFacerec
from professors import Professors
from datetime import datetime
import requests
import cv2

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("./face_recognition_system/images/")

prof = Professors()

student_names = ['Unknown']

# Load Camera
cap = cv2.VideoCapture(2)

currentFrame = 0

def sendMessage(token, chat_id, msg):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name_and_id in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
        name = str(name_and_id).split('_')[0]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)

        current_datetime = datetime.now()
        fr = '2024-10-20 08:00'
        to = '2024-10-20 19:30'

        if  fr <= str(current_datetime) <= to:
            if name not in student_names:
                student_names.append(name)
                sendMessage(prof.profMuhammadAftab['TOKEN'], prof.profMuhammadAftab['CHAT_ID'], f"{name_and_id}, {current_datetime}")

            '''
            match name:
                case name if name in profMuhammadAftab['students']:
                    if name not in student_names:
                        student_names.append(name)
                        sendMessage(profMuhammadAftab['TOKEN'], profMuhammadAftab['CHAT_ID'], f"{name_and_id}, {current_datetime}")
                        break
                case name if name in profJaydipMehta['students']:
                    if name not in student_names:
                        student_names.append(name)
                        sendMessage(profJaydipMehta['TOKEN'], profJaydipMehta['CHAT_ID'], f"{name_and_id}, {current_datetime}")
                        break
            '''

    cv2.imshow("Student attendance system", frame)
    cv2.imwrite(f'./generated_data/frame{str(currentFrame)}.jpg', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()