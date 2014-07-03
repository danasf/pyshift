# BBB pinout
# http://insigntech.files.wordpress.com/2013/09/bbb_pinouts.jpg
# test
from shifter import Shifter
import time


# DATA (R1), DATA2 (R2), CLOCK, LATCH, SelA, SelB, SelC,OE
s = Shifter("P8_7","P8_13","P8_9","P8_11","P8_8","P8_10","P8_12","P8_14")

while True:
        count = 0
        while count < 16:

                # select data pin 
                if count < 8:
                        pin = s.data1
                else:
                        pin = s.data2

                # select
                if count % 2 is 0:
                        s.sendBit(pin,True)
                        s.sendBit(pin,True)
                        s.sendBit(pin,False)
                        s.sendBit(pin,False)                        
                else:
                        s.sendBit(pin,False)
                        s.sendBit(pin,False)  
                        s.sendBit(pin,True)
                        s.sendBit(pin,True)
                
                s.latchData()
                s.selRow(count)
                count += 1

