import cv2
import uuid
cap = cv2.VideoCapture(0)
#capturing frame and providing result
result, frame = cap.read()
#radom uuid generation
name = str(uuid.uuid4())+".jpeg"
print(result)
#writting image to a file
cv2.imwrite(name,frame)
cap.release()
