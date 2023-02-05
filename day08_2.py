import cv2
# 이미지 읽어줘
def 이미지띄우기(img_path):
    img = cv2.imread('person.jpg')
# 이미지 보여줘
    cv2.imshow('title',img)
# 대기
    cv2.waitKey(0)

def ShowVideo(video_path):
    # 동영상 읽어줘
    vc = cv2.VideoCapture(video_path)
    # 무한반복 (동영상 == 빠르게 여러 이미지를 출력)
    while True:
        success, img = vc.read()
        if success:
            cv2.imshow('title',img)
            cv2.waitKey(20)
def ShowCam():
    vc = cv2.VideoCapture(0)
    vc.set(3,640)
    vc.set(4,480)

    while True:
        success, img = vc.read()
        if success:
            cv2.imshow('title',img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
            # esc 키를 눌러 종료

이미지띄우기('person.jpg')
