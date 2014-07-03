# Playing with Python, shift registers and BBB
# BBB pinout: http://insigntech.files.wordpress.com/2013/09/bbb_pinouts.jpg

import Adafruit_BBIO.GPIO as GPIO
import time

class Shifter(object):
        # init, 
        # data - is a single red pin at the moment
        # clk - clock pin
        # latch - latch
        # sel1,sel2,sel3 - row select bits 1 MSB, 3 LSB
        # oe - set high to supress display

        def __init__(self,data,clock,latch,sel1,sel2,sel3,oe):
                self.size = 32
                self.data = data
                self.clock = clock
                self.latch = latch
                self.sel1 = sel1
                self.sel2 = sel2
                self.sel3 = sel3
                self.oe = oe

                GPIO.setup(self.data, GPIO.OUT) # data RED1
                GPIO.setup(self.clock, GPIO.OUT) # clock
                GPIO.setup(self.latch, GPIO.OUT) # latch

                GPIO.setup(self.sel1, GPIO.OUT) # select bit 1
                GPIO.setup(self.sel2, GPIO.OUT) # select bit 2
                GPIO.setup(self.sel3, GPIO.OUT) # select bit 3
                GPIO.setup(self.oe, GPIO.OUT) # select bit 3

                GPIO.output(self.oe, GPIO.LOW) # set OE LOW

                GPIO.output(self.clock, GPIO.HIGH) # set clock HIGH
                GPIO.output(self.latch, GPIO.HIGH) # set latch HIGH

        # latch
        def latchData(self):
                GPIO.output(self.oe, GPIO.HIGH) # set OE LOW
                GPIO.output(self.latch,GPIO.HIGH)
                GPIO.output(self.latch,GPIO.LOW)
                #GPIO.output(self.latch,GPIO.HIGH)
                GPIO.output(self.oe, GPIO.LOW) # set OE LOW


        # send a single bit
        def sendBit(self,state):
                if state is True:
                        GPIO.output(self.data,GPIO.HIGH) # SET dat HIGH
                else:
                        GPIO.output(self.data,GPIO.LOW) # SET data LOW
                GPIO.output(self.clock,GPIO.LOW) # Clock to LOW
                GPIO.output(self.clock,GPIO.HIGH) # clock to HIGH

        # send line of bits
        def bitFill(self,filled):
                x = 0
                # while less than panel size
                while x < self.size-1:
                        # for up to filled value, on
                        for i in xrange(0,filled):
                                self.sendBit(True)
                                x += 1
                        # fill the rest of the bits, off        
                        for i in xrange(filled,self.size):
                                self.sendBit(False)
                                x +=1

        # set row(s) given decimal number
        def selRow(self,myState):
                
                if myState is 0:
                        self.select(False,False,False)
                elif myState is 1:
                        self.select(False,False,True)

                elif myState is 2:
                        self.select(False,True,False)

                elif myState is 3:
                        self.select(False,True,True)

                elif myState is 4:
                        self.select(True,False,False)

                elif myState is 5:
                        self.select(True,False,True)

                elif myState is 6:
                        self.select(True,True,False)

                elif myState is 7:
                        self.select(True,True,True)
                else:
                        self.select(False,False,False)

        # control select bits
        def select(self,state1,state2,state3):
                GPIO.output(self.oe, GPIO.HIGH) # set OE HIGH

                # Selector 1 MSB
                if state1 is True:
                        GPIO.output(self.sel1,GPIO.HIGH);
                else:
                        GPIO.output(self.sel1,GPIO.LOW);

                if state2 is True:
                        GPIO.output(self.sel2,GPIO.HIGH);
                else:
                        GPIO.output(self.sel2,GPIO.LOW);
                # Selector 3 LSB
                if state3 is True:
                        GPIO.output(self.sel3,GPIO.HIGH);
                else:
                        GPIO.output(self.sel3,GPIO.LOW);

                GPIO.output(self.oe, GPIO.LOW) # set OE LOW