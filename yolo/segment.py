import os 
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

model = YOLO('./yolo/weights/yolov8m-seg.pt')
names = model.model.names

input_video_path = './videos/security_camera.mp4'
output_video_path = f"./out/segment_{os.path.basename(input_video_path)}"

w, h = 720, 1200
cap = cv2.VideoCapture(input_video_path)
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (w, h))

while True:
    ret, im0 = cap.read()
    if not ret:
        print('Video frame is empty or video processing has been completed sucseccfully.')
        break
    im0 = cv2.resize(im0, (w, h))

    result = model.predict(im0)
    clss = result[0].boxes.cls.cpu().tolist()
    masks = result[0].masks.xy

    annotator = Annotator(im0, line_width=2)

    for mask, cls in zip(masks, clss):
        if names[int(cls) in ['person', 'car']]:
            try:
                annotator.seg_bbox(mask=mask, 
                                   mask_color=colors(int(cls), 
                                   True), det_label=names[int(cls)])

            except: continue

    out.write(im0)
    cv2.imshow('instance_segmentation', im0)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()