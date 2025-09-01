import cv2
import face_recognition
import numpy as np
import threading

known_face_encodings = []
known_face_names = []

Students = ['ZIYECH','BELHANDA','BOUSSOUFA','NSIRI']
Present = []
Absent = []
try:
    known_person2_image = face_recognition.load_image_file("./images/ziyech.jpg")
    known_person3_image = face_recognition.load_image_file("./images/belhanda.jpeg")
    known_person4_image = face_recognition.load_image_file("./images/bosofa.jpg")
    known_person5_image = face_recognition.load_image_file("./images/nseiri.jpeg")
    
    known_face_encodings.extend([
        face_recognition.face_encodings(known_person1_image)[0],
        face_recognition.face_encodings(known_person2_image)[0],
        face_recognition.face_encodings(known_person3_image)[0],
        face_recognition.face_encodings(known_person4_image)[0]
    ])
    known_face_names.extend(['ZIYECH','BELHANDA','BOUSSOUFA','NSIRI'])
except IndexError:
    print("One or more face encodings could not be generated. Check the images.")

video_capture = cv2.VideoCapture(0)
frame_count = 0
frame_skip = 5 
processed_frame = None
lock = threading.Lock()
Sure = 0
def process_frame(frame):
    global processed_frame
    global Sure
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    face_locations = face_recognition.face_locations(small_frame, model="cnn")
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        name = "Unknown"
        if face_distances[best_match_index] < 0.6:  
            if Sure < 3 :
                name = known_face_names[best_match_index]
                if name not in Present:
                    Present.append(name)
                Sure = 0
            else :
                Sure += 1
        
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    
    with lock:
        processed_frame = frame

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    if frame_count % frame_skip == 0:
        threading.Thread(target=process_frame, args=(frame.copy(),)).start()

    with lock:
        if processed_frame is not None:
            cv2.imshow("Video", processed_frame)

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        Absent = [studentName for studentName in Students if studentName not in Present]
        print(Students)
        print(Present)
        print(Absent)
        break

video_capture.release()
cv2.destroyAllWindows()
