import mediapipe as mp
import cv2

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

frame_path = './poseVideos/qolga_tayangan_holati_org.jpg'

frame = cv2.imread(frame_path)

frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
results = pose.process(frameRGB)

if results.pose_landmarks:
  mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
  for id, lm in enumerate(results.pose_landmarks.landmark):
    h, w, c = frame.shape
    cx, cy = int(lm.x*w), int(lm.y*h)
    
    cv2.circle(frame, (cx, cy), 3, (255, 0, 0), 2)

cv2.imwrite('./poseVideos/edited.jpg', frame)