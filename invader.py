# BBB pinout
# http://insigntech.files.wordpress.com/2013/09/bbb_pinouts.jpg
# space invader test
from shifter import Shifter
import time


frame1 = ["00001100000000000000000000000000","00011110000000000000000000000000","00111111000000000000000000000000","01101101100000000000000000000000","01111111100000000000000000000000","00010010000000000000000000000000","00101101000000000000000000000000","10100101000000000000000000000000"]
frame2 = ["00011000000000000000000000000000","00111100000000000000000000000000","01111110000000000000000000000000","11011011000000000000000000000000","11111111000000000000000000000000","00100100000000000000000000000000","01011010000000000000000000000000","01000010000000000000000000000000"]


# DATA (R1), DATA2 (R2), CLOCK, LATCH, SelA, SelB, SelC,OE
s = Shifter("P8_7","P8_13","P8_9","P8_11","P8_8","P8_10","P8_12","P8_14")
step = 0 # frame control
while True:
        count = 0
        pin = s.data1
        if step < 5:
                bitMap = frame1
        else:
                bitMap = frame2

        while count < 8:
                s.selRow(count)
                for c in bitMap[count]:
                        if c is "1":
                                s.sendBit(pin,True)
                        else:
                                s.sendBit(pin,False)
                s.latchData()
                count += 1

        step += 1
        if step > 10:
                step = 0
