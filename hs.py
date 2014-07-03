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
        while count < 16:
                s.selRow(count)
                if count < 8:
                        pin = s.data1
                else:
                        pin = s.data2

                for c in bitMap[count]:
                        if c is "1":
                                s.sendBit(pin,True)
                        else:
                                s.sendBit(pin,False)
                s.latchData()
                count += 1