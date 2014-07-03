# BBB pinout
# http://insigntech.files.wordpress.com/2013/09/bbb_pinouts.jpg
# matrix test
from shifter import Shifter
import time

bitMap = ["00111111110000000111100111100000","00000110000000001111111111110000","00000110000000000111111111100000","00000110000000000011111111000000","00000110000000000001111110000000","0$
# DATA (R1), DATA2 (R2), CLOCK, LATCH, SelA, SelB, SelC,OE
s = Shifter("P8_7","P8_13","P8_9","P8_11","P8_8","P8_10","P8_12","P8_14")
while True:
        count = 0
        pin = s.data1
        while count < 8:
                s.selRow(count)
                for x in xrange(0,31):
                        if bitMap[count][x] is "1":
                                s.sendBit(s.data1,True,False)
                        else:
                                s.sendBit(s.data1,False,False)

                        if bitMap[count+7][x] is "1":
                                s.sendBit(s.data2,True,False)
                        else:
                                s.sendBit(s.data2,False,False)
                        s.clockIn()
                s.latchData()
                count += 1