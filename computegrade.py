def computegrade(Score):
  if Score > .99:
    Grade = 'Score must be between 0.0 and 1.0'
  elif Score >= 0.9:
    Grade = 'A'
  elif Score >= 0.8:
    Grade = 'B'
  elif Score >= 0.7:
    Grade = 'C'
  elif Score >= 0.6:
    Grade = 'D'
  elif Score < 0.6:
    Grade = 'F'
  else:
    Grade = 'Score must be between 0.0 and 1.0'
  return Grade