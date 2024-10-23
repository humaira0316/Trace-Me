import face_recognition
import cv2
import numpy as np

def encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    return face_encodings[0] if face_encodings else None

def compare_faces(known_encoding, new_image_path):
    new_encoding = encode_image(new_image_path)
    if new_encoding:
        results = face_recognition.compare_faces([known_encoding], new_encoding)
        return results[0]
    return False
