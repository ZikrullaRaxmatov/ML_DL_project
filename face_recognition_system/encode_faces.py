import os
import face_recognition
import cv2
import numpy as np
import pickle

# Define the path to the directory containing known faces
KNOWN_FACES_DIR = "./face_recognition_system/known_faces/"
TOLERANCE = 0.6  # Distance between face encodings to consider a match
MODEL = "hog"  # "hog" or "cnn" for faster detection

# Prepare a list of known face encodings and names
known_face_encodings = []
known_face_names = []

# Loop through each person in the dataset
for person_name in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, person_name)

    for image_name in os.listdir(person_dir):
        image_path = os.path.join(person_dir, image_name)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]

        # Save the encoding and the person's name
        known_face_encodings.append(encoding)
        known_face_names.append(person_name)

# Save encodings to a file for later use
with open("face_encodings.pkl", "wb") as f:
    pickle.dump((known_face_encodings, known_face_names), f)
