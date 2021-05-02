 # Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import framebuf
import _thread
import math
import utime
import time
import drive_function
import oled_function
import distance_function

threshold = 40
front = 0
front_left = 0
front_right = 0
back = 0

uart = machine.UART(0)
message = "s"

drive_function.stop()

oled_function.show_text("Raspberry Pico",0,0)
utime.sleep(0.1)
oled_function.show_text("Startup",0,0)
utime.sleep(0.1)
oled_function.show_text("done",0,0)

def messure_distance():
    global front, front_left, front_right, back
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

# _thread.start_new_thread ( messure_distance , () )

while True:
    messure_distance()
    while uart.any():
        bytesdata = uart.readline()
        message = str (bytesdata )
        message = message.replace("b'", "")
        message = message.replace("\\r", "")
        message = message.replace("\\n", "")
        message = message.replace("'", "")
        print ( message )
        oled_function.show_text( message ,0,45)
    if message == "move":    
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
        message = "st"        
    if message == "st":
        drive_function.stop()
    if message == "fw":
        drive_function.forward()
    if message == "ll":
        drive_function.rotate_left()
    if message == "rr":
        drive_function.rotate_right()
    if message == "bb":
        drive_function.backward()
#utime.sleep(1)
