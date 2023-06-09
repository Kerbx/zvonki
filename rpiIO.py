import RPi.GPIO as GPIO


class IOControl:
    def __init__(self):
        self.ring = 13
        self.alarm = 16
        
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.ring, GPIO.OUT)
        GPIO.setup(self.alarm, GPIO.OUT)
        
        GPIO.output(self.ring, GPIO.HIGH)
        GPIO.output(self.alarm, GPIO.HIGH)
    
    def __del__(self):
        GPIO.output(self.ring, GPIO.HIGH)
        GPIO.output(self.alarm, GPIO.HIGH)
        
    def turnOn(self, pin):
        if pin == 'pin1':
            GPIO.output(self.ring, GPIO.LOW)
        elif pin == 'pin2':
            GPIO.output(self.alarm, GPIO.LOW)
    
    def turnOff(self, pin):
        if pin == 'pin1':
            GPIO.output(self.ring, GPIO.HIGH)
        elif pin == 'pin2':
            GPIO.output(self.alarm, GPIO.HIGH)
            
    def getState(self, pin):
        if pin == 'pin1':
            pass
        elif pin == 'pin2':
            return GPIO.input(self.alarm)
    