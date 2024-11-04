import cv2
import mediapipe as mp
import time 

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

input_video_path = './poseVideos/pose_mashq.mp4'

cap = cv2.VideoCapture(input_video_path)
pTime = 0
while cap.isOpened:
    ret, frame = cap.read()

    if not ret:
        print("Videoni o'qishda xatolik yoki yakunlandi!!!")
        break

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()

