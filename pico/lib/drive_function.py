from machine import Pin, PWM
import utime

motor1a = Pin(14, Pin.OUT)
motor1b = Pin(15, Pin.OUT)
motor2a = Pin(12, Pin.OUT)
motor2b = Pin(13, Pin.OUT)

pwm_motor1 = PWM( Pin( 10 ) )
pwm_motor1.freq(1000)
pwm_motor2 = PWM( Pin( 11 ) )
pwm_motor2.freq(1000)

def testdrive():
    print("testdrive")
    motor1a.low() #links forwärts
    motor1b.low() #links rückwärts
    motor2a.high() #rechts forwärts
    motor2b.high() #rechts rückwärts

def forward():
    print( "forward" )
#     return
    motor1a.high()
    motor1b.low()
    motor2a.high()
    motor2b.low()
    pwm_motor1.duty_u16(65000)
    pwm_motor2.duty_u16(65000)
    
def backward():
    print( "backward" )
#     return
    motor1a.low()
    motor1b.high()
    motor2a.low()
    motor2b.high()
    pwm_motor1.duty_u16(65000)
    pwm_motor2.duty_u16(65000)

def turn_back_left():
    motor1a.low()
    motor1b.high()
    motor2a.low()
    motor2b.low()
    pwm_motor1.duty_u16(40000)

def turn_back_right():
    motor1a.low()
    motor1b.low()
    motor2a.low()
    motor2b.high()
    pwm_motor2.duty_u16(40000)
    
def rotate_left():
    
    print( "rotate left" )
#     return
    motor1a.low()
    motor1b.high()
    motor2a.high()
    motor2b.low()
    pwm_motor1.duty_u16(40000)
    pwm_motor2.duty_u16(65000)
    utime.sleep(0.5)
    
def rotate_right():
    print( "rotate right" )
#     return
    motor1a.high()
    motor1b.low()
    motor2a.low()
    motor2b.high()
    pwm_motor1.duty_u16(65000)
    pwm_motor2.duty_u16(40000)
    utime.sleep(0.5)
    
def stop():
    print( "stop" )
    motor1a.low()
    motor1b.low()
    motor2a.low()
    motor2b.low()