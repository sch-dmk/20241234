import socket
import cv2
import numpy as np
BUF_SIZE = 8192
LENGTH = 10
videoFile = 'sch.mp4'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5000))
sock.listen(5)
while True:
    csock, addr = sock.accept()
    print('Client is connected')
    cap = cv2.VideoCapture(videoFile)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            temp = csock.recv (BUF_SIZE) #'start ' 수신
            if not temp:
                break
            result, imgEncode = cv2.imencode ('.jpg', frame)
            data = np.array(imgEncode)
            byteData = data.tobytes()
            csock.send(str(len(byteData)).zfill (LENGTH).encode ()) #10 개 문자열로 표현된 길이 전송
            temp = csock.recv (BUF_SIZE) #'image ' 수신
            if not temp:
                break
            csock.send(byteData)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    csock.close()