import cv2
import threading

RTSP_URL = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4'
streams=(
    [RTSP_URL,'cam1'],
    [RTSP_URL,'cam2'],
    [RTSP_URL,'cam3'],
)


def cams(s):
    url = s[0]
    cam = s[1]

    video = cv2.VideoCapture(url)
    while True:
        _, frame = video.read()
        cv2.imshow(cam, frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


thread_list = []
for s in streams:
    x = threading.Thread(target=cams, args=(s,))
    thread_list.append(x)
    # x.start()
    # x.join()

for thread in thread_list:
    # thread.setDaemon(True)
    thread.start()
    # thread.join()