# pose estimation

est = PoseEstimator()  #load the model
# take an image using the webcam (alternatively, you could load an image)
#cam = cv2.VideoCapture(0)
#for i in range(cv2.CAP_PROP_FRAME_COUNT):
#    cam.grab()
#ret, image = cam.retrieve()
#image = cv2.imread('/content/photo_2019-02-10_09-38-20.jpg')

def EstimatePose (image):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  #cam.release()
  #if est.pose_from_image(image) == True:
  roll, pitch, yawn = est.pose_from_image(image) # estimate the head pose
  #return roll, pitch, yawn
  # if roll:
  return roll
  #else:
  #  return 404
#est.plot_face_detection_marks(image)  # plot the image with the face detection marks
