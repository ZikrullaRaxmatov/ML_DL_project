import face_recognition
import cv2
import numpy as np
import pickle

# Load the known face encodings
with open("face_encodings.pkl", "rb") as f:
    known_face_encodings, known_face_names = pickle.load(f)

# Initialize the video capture object
video_capture = cv2.VideoCapture(0)

TOLERANCE = 0.6

while True:
    # Capture a single frame of video
    ret, frame = video_capture.read()

    # Resize the frame for faster face detection
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image to RGB color
    rgb_frame = small_frame[:, :, ::-1]

    # Detect faces and face encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop over each face in this frame
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare the face with the known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, TOLERANCE)

        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Scale back up face locations since the frame was scaled down
        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face and label it with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Quit the video by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()
