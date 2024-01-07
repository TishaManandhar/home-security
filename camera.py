import cv2
cap = cv2.VideoCapture(0)
result, frame = cap.read()
print(result)
cv2.imwrite("abc.jpeg",frame)
cap.release()
