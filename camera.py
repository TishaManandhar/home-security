import cv2
import uuid
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
print(weights)
print(boxes)
cap.release()
