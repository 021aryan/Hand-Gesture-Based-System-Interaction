import cv2
import face_recognition
import subprocess

# Load the saved image
known_image = face_recognition.load_image_file("kaushik.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize the video stream
video_capture = cv2.VideoCapture(0)
match_found = False

while True:
    # Read a single frame from the video stream
    ret, frame = video_capture.read()
    
    # Find all the faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Compare each detected face to the saved image
    for face_encoding, face_location in zip(face_encodings, face_locations):
        match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
        if match:
            # If there is a match, run another Python script
            print("face matched")
            subprocess.call(["python", "Nova.py"])
            match_found = True
            video_capture.release()
            cv2.destroyAllWindows()
            break

    
    # Display the current frame
    cv2.imshow('Video', frame)
    
    # Exit the loop if the 'q' key is pressed or face is matched
    if match_found or cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
video_capture.release()
cv2.destroyAllWindows()
