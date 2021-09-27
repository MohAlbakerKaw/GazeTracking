from detectGaze import detectGaze
from EAR import EAR
from EstimatePose import estimatePose



def main_front(image):
  rollv = estimatePose(image)
  EARv = EAR(image)
  Gazev = detectGaze(image)

  if EARv < 0.26:
    return 9

  else:
    if rollv != 404:
      if rollv < -20:
        return 0
      elif rollv > 20:
        return 4
      elif (20 > rollv > -20):
        return Gazev
      else:
        return Gazev
