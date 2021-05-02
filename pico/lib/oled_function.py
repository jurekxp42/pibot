from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

WIDTH  = 128
HEIGHT = 64

sda = Pin(20)
scl = Pin(21)
i2c = I2C( 0 , sda=sda, scl=scl, freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

def show_text ( text , left , top ):
    oled.fill(0) # Black
    oled.text( text , left , top )
    oled.show()
