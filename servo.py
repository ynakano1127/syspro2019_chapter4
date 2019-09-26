import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

def setservo(degree):
    servo.ChangeDutyCycle(middle + (12.0-7.2)*(degree/90.0))

setservo(0)
time.sleep(1.0)
setservo(15)
time.sleep(1.0)
setservo(30)
time.sleep(1.0)
setservo(45)
time.sleep(1.0)
setservo(60)
time.sleep(1.0)
setservo(90)
time.sleep(1.0)

setservo(0)
time.sleep(1.0)
setservo(-15)
time.sleep(1.0)
setservo(-30)
time.sleep(1.0)
setservo(-45)
time.sleep(1.0)
setservo(-60)
time.sleep(1.0)
setservo(-90)
time.sleep(1.0)
servo.stop()
GPIO.cleanup()
