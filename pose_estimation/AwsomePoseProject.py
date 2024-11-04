import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture('./videos/arjumaniya.mp4')

detector = pm.poseDetector()
pTime = 0
while True:
  success, frame = cap.read()

  if not success:
    print('Tamom')
    break

  frame = detector.findPose(frame)
  lmlist = detector.findPositions(frame)
  print(lmlist)

  cTime = time.time()
  fps = 1/(cTime - pTime)
  pTime = cTime

  cv2.putText(frame, str(int(fps)), (70, 50), 3, cv2.FONT_HERSHEY_PLAIN, (0, 255, 0), 3)
  #cv2.imshow('Frame', frame)
  cv2.waitKey(1)