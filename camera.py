import cv2
import uuid
cap = cv2.VideoCapture(0)
result, frame = cap.read()
name = str(uuid.uuid4())+".jpeg"
print(result)
cv2.imwrite(name,frame)
cap.release()
