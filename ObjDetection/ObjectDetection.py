import datetime
import cv2


# Youtube https://youtu.be/RFqvTmEFtOE
# OpenCV https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API
# frozen_model http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.tar.gz
# config_file https://gist.github.com/dkurt/54a8e8b51beb3bd3f770b79e56927bd7
# labels.txt in the video

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
file_name = 'labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')

print(classLabels)
print(len(classLabels))

model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot access video-feed")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

font = cv2.FONT_HERSHEY_PLAIN
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)

    text = str(datetime.datetime.now())[:-7]
    frame = cv2.putText(frame, text, (10, height - 20), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
    # cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font, fontScale=3,
    # color=(255, 255, 255))

    print(ClassIndex)
    if len(ClassIndex) != 0:
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            if ClassInd <= 80:
                cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                out.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
