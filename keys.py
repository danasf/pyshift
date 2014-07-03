from shifter import Shifter
import time
import sys
row=0
# DATA (R1), DATA2 (R2), CLOCK, LATCH, SelA, SelB, SelC,OE
s = Shifter("P8_7","P8_13","P8_9","P8_11","P8_8","P8_10","P8_12","P8_14")

while True:
        counter=0;
        s.selRow(row)
        while counter < 31:
                char = raw_input("Press Q for on W for Off")
                print "You pressed %s" % char

                if char is 'q':
                        print "row: %i  bit: %i  state: On" % (row,counter)
                        s.sendBit(s.data1,True)
                        counter += 1
                elif char is 'w':
                        print "row: %i  bit: %i  state: Off" % (row,counter)
                        s.sendBit(s.data1,False)
                        counter += 1
                elif char is 'r':
                        #s.latchData()
                        print "new row"
                        break
                elif char is 'e':
                        s.bitFill(s.data1,0)
                        s.latchData()
                else:
                        print "key not recognized"

        if row > 7:
                row = 0
        else:
                row +=1
