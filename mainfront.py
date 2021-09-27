def main_front(image):
  rollv = EstimatePose(image)
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
