import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0)


def detect_person():
    # capturing frame and providing result
    result, frame = cap.read()
    if result:
        #frame = cv2.resize(frame, (640, 480))
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))
        #cv2.imshow('frame', frame)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        boxes, weights = hog.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.05)
        if len(boxes) > 0:
            return True
        else:
            return False
    else:
        print("Could not capture frame")
        return False



