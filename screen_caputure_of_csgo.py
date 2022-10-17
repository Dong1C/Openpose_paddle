import time
import pyautogui
from pynput.keyboard import Key, Controller
import cv2
import mss
import numpy
import pyautogui as pa
import time
import pydirectinput as pt
key = Controller()


def startgame():
    key.release(Key.space)


import sys

sys.path.append('E:/Coding_Python/openpose-paddle/openpose')

# startgame()
from openpose.detectors.detector import PoseDetector
from openpose.util import draw_pose

detector = PoseDetector(pose_points=25, detect_face=False, detect_hand=False)

with mss.mss() as sct:
    # Part of the screen to capture
    w, h = 2160, 1440
    monitor = {'top': 720 - int(h / 2), 'left': 1080 - int(w / 2), 'width': w, 'height': h}

    while 1:
        # key.press(Key.down)
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        # cv2.imshow('title', img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        heat_img = numpy.array(detector(img))
        for i in range(25):
            # (0, 0) if not heat_img else
            xoffset, yoffset = (0,0) if not heat_img[0] else list(heat_img[0].values())[:-1][0][i]
            if xoffset < 0 or yoffset < 0:
                continue
            xoffset, yoffset = xoffset - 1080, yoffset -720
            #pt.moveTo(int(xoffset/26),  int(yoffset/40),duration=1)
            pt.Click()
            #print(list(heat_img[0].values()))
