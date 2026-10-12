import cv2
import numpy as np
import face_recognition
import pickle


def register_face(name):
    video_capture = cv2.VideoCapture(0)

    print(f"Registering face for {name}... Look at the camera.")
    face_encodings_list = []

    while True:
        ret, frame = video_capture.read()
        if not ret:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        if face_encodings:
            print("Face detected! Capturing face data...")
            face_encodings_list.append(face_encodings[0])

            if len(face_encodings_list) >= 5:  # Capture multiple encodings for accuracy
                break

        cv2.imshow("Register Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    try:
        with open("faces_data.pkl", "rb") as file:
            known_faces = pickle.load(file)
    except FileNotFoundError:
        known_faces = {"names": [], "encodings": []}

    known_faces["names"].append(name)
    known_faces["encodings"].append(np.mean(face_encodings_list, axis=0))  # Store average encoding

    with open("faces_data.pkl", "wb") as file:
        pickle.dump(known_faces, file)

    print(f"Face for {name} registered successfully!")


if __name__ == "__main__":
    register_face("Kaze")  # Change name if needed
