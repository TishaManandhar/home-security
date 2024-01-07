import cv2
import uuid
import numpy as np
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0)
#capturing frame and providing result
result, frame = cap.read()
#radom uuid generation
name = str(uuid.uuid4())+".jpeg"

print(result)
#writting image to a file
cv2.imwrite(name,frame)
frame = cv2.resize(frame, (640,480))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
boxes,weights = hog.detectMultiScale(gray, winStride=(8,8))
boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(gray, (xA, yA), (xB, yB), (0, 255, 0), 2)
if len(boxes) > 0:
    print(weights)
    print(boxes)
    print("Person Detected.")
    cv2.imwrite(str(uuid.uuid4())+"-detected.jpeg", gray)
else:
    print("Person Not Detected.")
cap.release()
