# importing Libraries
import cv2
from google.colab.patches import cv2_imshow
import dlib
from scipy.spatial import distance

from headpose import PoseEstimator

from gaze_tracking import GazeTracking


import time
import math

# Eye Aspect Ratio

# defining Functions
def calculate_EAR(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear_aspect_ratio = (A+B)/(2.0*C)
	return ear_aspect_ratio

hog_face_detector = dlib.get_frontal_face_detector()
datFile =  "/content/shape_predictor_68_face_landmarks.dat"
dlib_facelandmark = dlib.shape_predictor(datFile)


def EAR(frame):
  # converting to gray
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # detecting faces
  faces = hog_face_detector(gray)

  for face in faces:
    face_landmarks = dlib_facelandmark(gray, face)
    leftEye = []
    rightEye = []

    for n in range(36,42):
      x = face_landmarks.part(n).x
      y = face_landmarks.part(n).y
      leftEye.append((x,y))
      next_point = n+1
      if n == 41:
        next_point = 36
      x2 = face_landmarks.part(next_point).x
      y2 = face_landmarks.part(next_point).y
      cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)          

    for n in range(42,48):
        x = face_landmarks.part(n).x
        y = face_landmarks.part(n).y
        rightEye.append((x,y))
        next_point = n+1
        if n == 47:
          next_point = 42
        x2 = face_landmarks.part(next_point).x
        y2 = face_landmarks.part(next_point).y
        cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

    left_ear = calculate_EAR(leftEye)
    right_ear = calculate_EAR(rightEye)
    EAR = (left_ear+right_ear)/2
    EAR = round(EAR,2)

    #if EAR<0.26:
      #cv2.putText(frame,"DROWSY",(20,100),
      #  		cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
      #cv2.putText(frame,"Are you Sleepy?",(20,400),
      #      cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
    #  print(EAR)
    #else: 
      #cv2.putText(frame,"ALERT",(20,100),
      #  		cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,0),4)      
    #  print(EAR)
    return EAR
    #cv2_imshow(frame)
    
