#!/usr/bin/env python3
import i2clcd

lcd = i2clcd.i2clcd(i2c_bus=1, i2c_addr=0x27, lcd_width=16)
lcd.init()
lcd.print_line('hello', line=0)
lcd.set_backlight(0)
lcd.set_backlight(1)

lcd.print_line('goodbye', line=1)

lcd.print_line('test', 1, 'center')


if __name__ == "__main__":
	try:
		setup()
	except KeyboardInterrupt:
		destroy()
