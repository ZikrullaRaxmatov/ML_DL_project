import mediapipe as mp
import cv2

frame = cv2.imread('../pose_estimation/poseVideos/qolga_tayangan_holati_org.jpg')

cv2.imshow('Imaage', frame)

cv2.waitKey(1)