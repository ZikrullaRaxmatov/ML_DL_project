import cv2
import mediapipe as mp
import time

class poseDetector():

  def __init__(self, mode=False, upBody=False, smooth=True, detectionConf=0.5, trackingConf=0.5):
    self.mode = mode
    self.upBody = upBody
    self.smooth = smooth
    self.detectionConf = detectionConf
    self.trackingConf = trackingConf

    self.mpDraw = mp.solutions.drawing_utils
    self.mpPose = mp.solutions.pose
    self.pose = self.mpPose.Pose(self, self.mode, self.upBody, self.smooth, self.detectionConf, self.trackingConf)


  def findPose(self, frame, draw=True):
    imgRBG = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = self.pose.process(imgRBG)

    if results.pose_landmarks:
      if draw:
        self.mpDraw.draw_landmarks(frame, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
  
    return frame

  def findPositions(self, frame, draw=True):

    if self.results.pose_landmarks:
      lmList = []
      for id, lm in enumerate(self.results.pose_landmarks.landmark):
        h, w, c = frame.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        lmList.append([id, cx, cy])
        if draw:
          cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
    return frame        


def main():
  cap = cv2.VideoCapture('./videos/mashq.mp4')
  
  detector = poseDetector()
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

if __name__ == "__main__":
  main()
