import numpy as np
import cv2 as cv

def get_limits(color):
    c = np.uint8([[color]])
    hsv_color = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    lower_limit = hsv_color[0][0][0] - 10, 100, 100
    upper_limit = hsv_color[0][0][0] + 10, 255, 255

    lower_limit = np.array([lower_limit], dtype=np.uint8)
    upper_limit = np.array([upper_limit], dtype=np.uint8)
    return lower_limit, upper_limit

def get_mask(frame, lower_limit, upper_limit):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower_limit, upper_limit)
    return mask
