# Playing with Python, shift registers and BBB
# BBB pinout: http://insigntech.files.wordpress.com/2013/09/bbb_pinouts.jpg

import Adafruit_BBIO.GPIO as GPIO
import time

class Shifter(object):
        # init, 'data' is a single red pin at the moment
        def __init__(self,data,clock,latch,sel1,sel2,sel3):
                self.size = 32
                self.data = data
                self.clock = clock
                self.latch = latch
                self.sel1 = sel1
                self.sel2 = sel2
                self.sel3 = sel3

                GPIO.setup(self.data, GPIO.OUT) # data RED1
                GPIO.setup(self.clock, GPIO.OUT) # clock
                GPIO.setup(self.latch, GPIO.OUT) # latch

                GPIO.setup(self.sel1, GPIO.OUT) # select bit 1
                GPIO.setup(self.sel2, GPIO.OUT) # select bit 2
                GPIO.setup(self.sel3, GPIO.OUT) # select bit 3

                GPIO.output(self.clock, GPIO.HIGH) # set clock HIGH
                GPIO.output(self.latch, GPIO.HIGH) # set latch HIGH

        # control select bits
        def select(self,state1,state2,state3):
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
        # latch
        def latchData(self):
                GPIO.output(self.latch,GPIO.HIGH)
                GPIO.output(self.latch,GPIO.LOW)

        # send a bit
        def sendBit(self,state):
                if state is True:
                        GPIO.output(self.data,GPIO.HIGH) # SET dat HIGH
                else:
                        GPIO.output(self.data,GPIO.LOW) # SET data LOW
                GPIO.output(self.clock,GPIO.LOW) # Clock to LOW
                GPIO.output(self.clock,GPIO.HIGH) # clock to HIGH

        # send line of bits
        def bitArrayFill(self,filled):
                x = 0
                while x < self.size:
                        for i in xrange(0,filled):
                                self.sendBit(True)
                                x += 1
                        for i in xrange(filled,self.size):
                                self.sendBit(False)
                                x +=1
        # if number is even return true, else false
        def isEven(self,num):
                if num % 2 is 0:
                        return True
                else:
                        return False

