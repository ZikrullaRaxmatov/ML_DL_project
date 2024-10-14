import cv2
import requests
from datetime import datetime
from simple_facerec import SimpleFacerec

TOKEN = '8136431001:AAFj_QR82MMDwy9Pdke0uirE_4T6C-6tqtI'
CHAT_ID = '755982207'

def sendMessage(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    r = requests.get(url)

student_names = ['Unknown']

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("./face_recognition_system/images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)

        current_datetime = datetime.now()

        if name not in student_names:
            student_names.append(name)
            sendMessage(f"{name}, {current_datetime}")
            

    cv2.imshow("Student attendance system", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()