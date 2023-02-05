import cv2
import mediapipe as mp



cap = cv2.VideoCapture('video.mp4')
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection(0.5)


while True:
    success, img = cap.read()
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        face = fd.process(from_bgr_to_rgb)
        if face.detections:
            for id, detection in enumerate(face.detections):
                fd_box = detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]),\
                    int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])
                cv2.rectangle(img,box,(255,0,255),2)
                cv2.putText(img,f'{round(detection.score[0]*100,1)}%',(box[0],box[0]),cv2.FONT_ITALIC,2,(255,0,255),2)
        


        cv2.imshow('title',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break























face = fd.process(from_bgr_to_rgb)

if face.detections:
    for id, detection in enumerate(face.detections):
        fd