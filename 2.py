import smbus 
import time
bus = smbus.SMBus(1) 
DEVICE = 0x20 
IODIRA = 0x00 
OLATA = 0x14 
GPIOA = 0x12 
bus.write_byte_data
bus.write_byte_data
for MyData in range(1,8):
	bus.write_byte_data(DEVICE,OLATA,MyData)
	print(MyData) 
	time.sleep(1) 
	bus.write_byte_data(DEVICE,OLATA,0)
