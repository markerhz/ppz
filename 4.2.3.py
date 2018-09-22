import RPi.GPIO as GPIO
import time
import smbus
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
blink = GPIO.PWM(27,500)
multiply = 1
duty = 0
counttime=0;
st=0
blink.start(duty)
bus = smbus.SMBus(1) #(512MB)
addr = 0x23 # i2c adress
while True:
	da=datetime.datetime.now()
	microsec=da.microsecond
if microsec > 700000:
 blink.ChangeDutyCycle(st)
else:
 blink.ChangeDutyCycle(0)
data = bus.read_i2c_block_data(addr,0x11)
lum=(data[1] + (data[0]<<8) / 1.2)
if lum<90:
 st=50
else:
 st=0
time.sleep(0.2) 
