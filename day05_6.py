# import가 안되는 이유 : 설치가 안된 라이브러리(모듈) 또는 오타
# pip install opencv-python
import cv2

# 이미지 = cv2.imread('img1.png') #이미지 보여줘
# cv2.imshow('title', 이미지)     # 보여줘

# cv2.waitKey(0)      # 무한대기







def cv_img(path):
    이미지2 = cv2.imread(path)
    cv2.imshow('title', 이미지2)
    cv2.waitKey(0)


cv_img('img3.jpg')