from machine import Pin
import math
import utime

trigger_front_right = Pin(2, Pin.OUT)
echo_front_right = Pin(3, Pin.IN)

trigger_front = Pin(4, Pin.OUT)
echo_front = Pin(5, Pin.IN)

trigger_front_left = Pin(6, Pin.OUT)
echo_front_left = Pin(7, Pin.IN)

trigger_back = Pin(16, Pin.OUT)
echo_back = Pin(17, Pin.IN)

def distance_front_right():
    return math.floor( get_distance ( trigger_front_right , echo_front_right ) )
    
def distance_front():
    return math.floor( get_distance ( trigger_front , echo_front ) )
    
def distance_front_left():
    return math.floor( get_distance ( trigger_front_left , echo_front_left ) )
    
def distance_back():
    return math.floor( get_distance ( trigger_back , echo_back ) )
    

def get_distance( trigger, echo ):
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    signaloff = 0
    signalon = 0
    timepassed = 0
    while echo.value() == 0:
       signaloff = utime.ticks_us()
    while echo.value() == 1:
       signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance =(timepassed/2) / 29.1
    return distance