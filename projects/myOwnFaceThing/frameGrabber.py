from PIL import Image
import cv2
import numpy
vc = cv2.VideoCapture('./MilkyWay.mp4')
frameNum = 2
im_size = (int(vc.get(cv2.CAP_PROP_FRAME_COUNT)),1080)
composite = Image.new("RGB", im_size)
while True:
    ret,frame = vc.read()
    if frame is None:
        break
    currCap = frame[0:1080,frameNum-2:frameNum]
    currCapPIL = Image.fromarray(currCap)
    composite.paste(currCapPIL,(frameNum,0))
    total = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
    frameNum += 2
composite.save("MilkyWay.jpeg", "JPEG")
print('done')
vc.release()
cv2.destroyAllWindows