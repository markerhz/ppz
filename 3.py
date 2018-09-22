import smbus
import time
bus = smbus.SMBus(1) 
DEVICE = 0x20 
IODIRA = 0x00 
OLATA = 0x14 
GPIOA = 0x12 
GPPUA = 0x0C 
bus.write_byte_data(DEVICE,IODIRA,0x80) 
bus.write_byte_data(DEVICE,GPPUA,0x80) 
while True: 
	MySwitch = bus.read_byte_data(DEVICE,GPIOA) 
	if(MySwitch & 0b10000000 == 0b00000000): 
		bus.write_byte_data(DEVICE,OLATA,0b10000001)
		print("Switch was pressed!")
		time.sleep(0.5)
	else:
		bus.write_byte_data(DEVICE,OLATA,0b10000000)
