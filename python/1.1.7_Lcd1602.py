#!/usr/bin/env python3
import LCD1602
import time

def setup():
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.write(0, 0, 'Hello Meredith')
	LCD1602.write(1, 1, 'How are you?')
	time.sleep(10)
	destroy()

def destroy():
	LCD1602.clear()

if __name__ == "__main__":
	try:
		setup()
	except KeyboardInterrupt:
		destroy()
