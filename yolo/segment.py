import os 
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, color 

model = YOLO('./yolo/yolov8m-seg.pt')
names = model.model.names

