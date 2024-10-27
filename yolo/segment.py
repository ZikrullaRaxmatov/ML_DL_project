from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import os 
import cv2

#creating model 
model = YOLO('./yolo/weights/yolov8m-seg.pt')
names = model.model.names

# input and output path
input_video_path = './yolo/videos/one_way_traffic.mp4'
output_video_path = f"./yolo/out/segment_{os.path.basename(input_video_path)}"

#read video
cap = cv2.VideoCapture(input_video_path)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (w, h))

while True:
  ret, img = cap.read()

  if not ret:
    print('Video yakunlandi!!!')
    break
  
  img = cv2.resize(img, (w, h))

  results = model.predict(img)
  clss = results[0].boxes.cls.cpu().tolist()
  masks = results[0].masks.xy

  annotator = Annotator(img, line_width=2)

  for  mask, cls in zip(masks, clss):
    if names[int(cls) in ['car', 'track']]:
      try:
        annotator.seg_bbox(mask=mask, mask_color=colors, label=names[int(cls)])
      except: continue

  out.write(img)
  #cv2.imshow('instance-segmentation', img)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  

cap.release()
out.release()
cv2.destroyAllWindows()