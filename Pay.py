try:
  Hours = input('Enter Hours: ')
  Rate = input('Enter Rate: ')
  RateOvr40 = Rate * 0.5
  Ovr40 = Hours - 40
  Pay = (Hours * Rate) + (RateOvr40 * Ovr40)
  print Pay
except:
  print 'Please enter numbers for Hours and Rate'