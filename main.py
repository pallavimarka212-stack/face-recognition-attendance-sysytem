import cv2
import os
from deepface import DeepFace
from datetime import datetime

path = 'dataset'

# ✅ UPDATED attendance function (Name, Date, Time)
def markAttendance(name):
    file_path = os.path.join(os.getcwd(), "attendance.csv")

    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')

    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a+') as f:
        f.seek(0)
        data = f.readlines()

        # Add header if file is empty
        if not file_exists or len(data) == 0:
            f.write("Name,Date,Time\n")

        names = [line.split(',')[0] for line in data]

        if name not in names:
            f.write(f"{name},{date},{time}\n")
            print("Saved:", name, date, time)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Save temporary image
    cv2.imwrite("temp.jpg", frame)

    for img in os.listdir(path):
        try:
            result = DeepFace.verify("temp.jpg", f"{path}/{img}", enforce_detection=False)

            if result['verified']:
                name = os.path.splitext(img)[0].upper()
                print("Matched:", name)

                markAttendance(name)

                cv2.putText(frame, name, (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except:
            pass

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == 13:  # Press Enter to stop
        break

cap.release()
cv2.destroyAllWindows()