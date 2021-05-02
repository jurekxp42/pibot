#!/usr/bin/python

from __future__ import division
import time
import Adafruit_PCA9685
import sys

pwm = Adafruit_PCA9685.PCA9685()

servo1_min = 340  #unterste Stellung
servo1_max = 520  #oberste Stellung
servo2_min = 390  #unterste Stellung
servo2_max = 240  #oberste Stellung
hand_open = 500
hand_close = 710

pwm.set_pwm_freq(60)

def move_servo ( no , start , end ):
	print ( str(start)+" : "+str(end) )
	if start < end:
		for i in range( start , end , 10 ):
			pwm.set_pwm( no , 0 , i )
			time.sleep( 0.05 )
	else:
		for i in range( start , end , -10 ):
			pwm.set_pwm( no , 0 , i )
			time.sleep( 0.05 )
	
def arm1_down():
	move_servo( 0, servo1_max , servo1_min )
def arm1_up():
	move_servo( 0 , servo1_min , servo1_max )
	
def arm2_down():
	move_servo( 1, servo2_max , servo2_min )
def arm2_up():
	move_servo( 1 , servo2_min , servo2_max )

def open_hand():
	move_servo ( 2 , hand_close , hand_open )
def close_hand():
	move_servo ( 2 , hand_open , hand_close )

def sleep():
	close_hand()
	arm1_up()
	arm2_down()

def greifen():
	open_hand()
	arm1_down()
	arm2_down()
	time.sleep(0.5)
	
	close_hand()
	arm2_up()
	arm1_up()
	time.sleep(0.5)

print (sys.argv[1] )
#try:
if sys.argv[1] == "greifen":
	greifen()

if sys.argv[1] == "sleep":
	sleep()

if sys.argv[1] == "fw":
	
#except KeyboardInterrupt:
#	open_hand()
#	arm2_up()
#	arm1_up()
#	pass
	
	
