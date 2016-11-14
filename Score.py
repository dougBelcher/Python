try:
  Score = input('Enter score between 0.0 and 1.0: ')
  if Score > .99:
    print 'Bad score'
  elif Score >= 0.9:
    print 'A'
  elif Score >= 0.8:
    print 'B'
  elif Score >= 0.7:
    print 'C'
  elif Score >= 0.6:
    print 'D'
  elif Score < 0.6:
    print 'F'
  else:
    print 'Score must be between 0.0 and 1.0'
except:
  print 'Bad score'	