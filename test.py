import time
class Robot:
    Pin1=14
    Pin2=15
    PinE=18
    PinS=23
    StAngle=25
    GPIO.setup(Pin1,GPIO.output)
    GPIO.setup(Pin2,GPIO.output)
    GPIO.setup(PinE,GPIO.output)
    GPIO.setup(PinS,GPIO.output)
    Pwm=GPIO.PWM(PinE,100)
    PwmS=GPIO.PWM(PinS,100)
    Pwm.start(30)
    PwmS.start(StAngle)
    
    def Speed(self):
        Pwm.ChangeDutyCycle()
    def Stop(self):
        GPIO.output(Pin1,GPIO.LOW)
        GPIO.output(Pin2,GPIO.LOW)
        GPIO.output(PinE,GPIO.LOW)
    def MoveForward(self,duration=0):
        if duration!=0:
            GPIO.output(Pin1,GPIO.HIGH)
            GPIO.output(Pin2,GPIO.LOW)
            GPIO.output(PinE,GPIO.HIGH)
        else:
            GPIO.output(Pin1,GPIO.HIGH)
            GPIO.output(Pin2,GPIO.LOW)
            GPIO.output(PinE,GPIO.HIGH)
            time.sleep(duration)
            self.Stop()
    def MoveBackwards(self,duration=0):
       if duration!=0:
            GPIO.output(Pin1,GPIO.LOW)
            GPIO.output(Pin2,GPIO.HIGH)
            GPIO.output(PinE,GPIO.HIGH)
        else:
            GPIO.output(Pin1,GPIO.LOW)
            GPIO.output(Pin2,GPIO.HIGH)
            GPIO.output(PinE,GPIO.HIGH)
            time.sleep(duration)
            self.Stop()
    def MoveRight(self):
        if self.StAngle ==5 : 
            return
        else:
            self.StAngle=self.StAngle-20
            self.PwmS.ChangeDutyCycle(self.StAngle)
    def MoveRight(self):
        if self.StAngle ==45 : 
            return
        else:
            self.StAngle=self.StAngle+20
            self.PwmS.ChangeDutyCycle(self.StAngle)
    def CleanUp(self):
        GPIO.cleanup() 

