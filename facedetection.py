import cv2
import numpy as np
import face_recognition
import pickle

def load_face_data():
    try:
        with open("faces_data.pkl", "rb") as file:
            known_faces = pickle.load(file)
        return known_faces
    except FileNotFoundError:
        return None

def detect_faces():
    known_faces = load_face_data()

    if not known_faces:
        print("No stored face data found. Please register your face first.")
        return False

    video_capture = cv2.VideoCapture(0)
    print("Looking for a face...")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces["encodings"], face_encoding, tolerance=0.5)
            face_distances = face_recognition.face_distance(known_faces["encodings"], face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index] and known_faces["names"][best_match_index] == "Kaze":
                print("Face Matched: Kaze")
                video_capture.release()
                cv2.destroyAllWindows()
                return True

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    print("Unauthorized face detected. Access denied.")
    return False

# if __name__ == "__main__":
#     print("Detecting face...")
#     stored_faces = load_face_data()
#
#     if stored_faces:
#         detected_person = detect_faces()  # Get detected face's name
#         if detected_person:
#             print(f"Face recognized: {detected_person}")
#
#         if detected_person == "Kaze":  # Allow only Kaze
#             print(f"Access granted: {detected_person}")
#             from wishme import wishme
#             wishme()
#         else:
#             print("Unauthorized person detected! Access denied.")
#             exit()
#     else:
#         print("No stored face data found. Please register your face first.")
#
