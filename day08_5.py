# opencv 모듈추가
# mediapipe 모듈 추가

# 이미지 
# 동영상 

import cv2
import mediapipe

def 이미지(hi_img):
    img = cv2.imread('person3.jpg')
    cv2.imshow('title',img)
    cv2.waitKey(0)

# 이미지('person.jpg')

def ShowVideo(video):
    vc = cv2.VideoCapture(video)
    while True:
        success, img = vc.read()
        if success:
            cv2.imshow('title',img)
            cv2.waitKey(20)
ShowVideo('video2.mp4')