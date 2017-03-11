# import required libs
import time
import RPi.GPIO as GPIO

 
# Use BOARD references
GPIO.setmode(GPIO.BOARD)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
StepPins = [37,35,33,31]
 
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

#wait some time to start
time.sleep(0.5)
 
# Define some settings
StepCounter = 0
WaitTime = 3.0/2000
 
# Define simple sequence
StepCount1 = 4
Seq1 = [0,0,0,0]
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]
 
# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = [0]*8
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

#Full torque
StepCount3 = 4
Seq3 = [0,0,0,0]
Seq3[0] = [0,0,1,1]
Seq3[1] = [1,0,0,1]
Seq3[2] = [1,1,0,0]
Seq3[3] = [0,1,1,0]
 
# set
Seq = Seq2
StepCount = StepCount2
 
# Start main loop
try:
  while True:
    for pin in range(0, 4):
      xpin = StepPins[pin]
      if Seq[StepCounter][pin]!=0:
        #print " Step %i Enable %i" %(StepCounter,xpin)
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)
    StepCounter += 1

  # If we reach the end of the sequence
  # start again
    if (StepCounter==StepCount):
      StepCounter = 0
    if (StepCounter<0):
      StepCounter = StepCount
 
  # Wait before moving on
    time.sleep(WaitTime)
except:
  #GPIO.cleanup();
  pass
finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
  GPIO.cleanup();
