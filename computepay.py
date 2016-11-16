def computepay(Hours, Rate):
  RateOvr40 = Rate * 0.5
  if Hours >= 40:
    Ovr40 = Hours - 40
  else: Ovr40 = 0
  Pay = (Hours * Rate) + (RateOvr40 * Ovr40)
  return Pay