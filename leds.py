# BBB pinout
# http://insigntech.files.wordpress.com/2013/09/bbb_pinouts.jpg

from shifter import Shifter
import time


# DATA (R1), CLOCK, LATCH, SelA, SelB, SelC
s = Shifter("P8_7","P8_9","P8_11","P8_8","P8_10","P8_12")
count = 0
# set to off
s.bitArrayFill(0)
while True:
        myState = s.isEven(count)
        for x in xrange(0,32):
                fillRow(s,1)
                s.latchData()

        count += 1


# simple cycle on and off
def onOff(s,delay):
        
# fill row
def fillRow(s,delay):
        print "filling with", x, "HIGH bits"
        s.bitArrayFill(x)
        s.latchData()
        time.sleep(delay)



