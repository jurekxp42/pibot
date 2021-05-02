 # Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import framebuf
import math
import utime
import time
import drive_function
import oled_function
import distance_function

threshold = 30

drive_function.stop()

oled_function.show_text("Raspberry Pico",0,0)
utime.sleep(0.1)
oled_function.show_text("Startup",0,0)
utime.sleep(0.1)
oled_function.show_text("done",0,0)

while True:
    
    front_right =  distance_function.distance_front_right() 
    utime.sleep(0.1)
    front = distance_function.distance_front() 
    utime.sleep(0.1)
    front_left = distance_function.distance_front_left()
    utime.sleep(0.1)
    back = distance_function.distance_back()
    message = str(front_right)+":"+str(front)+":"+str(front_left)+":"+str(back)
    print ( message )
    oled_function.show_text( message ,0,25)
    

    if back < 20 :
        drive_function.stop()
        utime.sleep( 1 )
        drive_function.forward()
    elif front_left > threshold and front > threshold and front_right > threshold:
        drive_function.forward()
    elif front_left < threshold and front > threshold and front_right > threshold:
        drive_function.stop()
        utime.sleep( 1 )
        drive_function.backward()
        utime.sleep( 0.3 )
        drive_function.rotate_right()
        utime.sleep( 0.3 )
        drive_function.forward()
    elif front_left > threshold and front > threshold and front_right < threshold:
        drive_function.stop()
        utime.sleep( 1 )
        drive_function.backward()
        utime.sleep( 0.3 )
        drive_function.rotate_left()
        utime.sleep( 0.3 )
        drive_function.forward()
    elif front < threshold:
        drive_function.stop()
        utime.sleep( 1 )
        drive_function.backward()
        utime.sleep( 0.4 )
        drive_function.rotate_left()
        utime.sleep( 1 )
        drive_function.forward()
    else:
        drive_function.stop()
    utime.sleep(0.1)
