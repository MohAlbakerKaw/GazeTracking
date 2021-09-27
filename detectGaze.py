from gaze_tracking import GazeTracking
# gaze tracking 

gaze = GazeTracking()
def detectGaze(frame):
  gaze.refresh(frame)
  if gaze.is_right():
    #text = "Looking right"
    return 3
  elif gaze.is_left():
    #text = "Looking left"
    return 1
  elif gaze.is_center():
    #text = "Looking center"
    return 2
  #elif gaze.is_blinking():
  #  text = "blinking"
  else:
    #text = "no answer"
    return 404
  # return text
