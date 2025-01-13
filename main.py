import cv2 as cv
from util import get_limits
from PIL import Image

# reading webcam
webcam = cv.VideoCapture(0)
address = "http://****.**.***/video"
webcam.open(address)

yellow = [0, 255, 255]

# visualizing images
ret = True

while ret:
    ret, frame = webcam.read()#if the frames are properly read then it will be true

    lower_limit, upper_limit = get_limits(yellow)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_limit, upper_limit)
    
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)


    cv.imshow('frame',frame)
    if cv.waitKey(40) & 0xFF == ord('q'):
        break


webcam.release()
cv.destroyAllWindows()