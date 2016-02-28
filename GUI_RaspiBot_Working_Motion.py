from gpiozero import LED
import picamera
from time import sleep
from tkinter import *
import random

root = Tk()
led1 = LED(17)
led2 = LED(24)
led3 = LED(23)
led4 = LED(27)
i = 0
camera = picamera.PiCamera()
myFile1 = "/home/pi/BotPics/raspiCam"
random1 = random(1, 99999)
myFile2 = ".jpg"


def turn_right():
    led1.on()
    led2.on()
    sleep(.18)
    led1.off()
    led2.off()

def turn_left():
    led3.on()
    led4.on()
    sleep(.18)
    led3.off()
    led4.off()

def move_forward():
    led1.on()
    led3.on()
    sleep(1)
    led1.off()
    led3.off()

def move_back():
    led2.on()
    led4.on()
    sleep(1)
    led2.off()
    led4.off()

def snap_pic():
    camera.capture(myFile1, random1, myFile2)

Label(text="Raspi Remote").grid(row=0, column=2, sticky=N)
Button(root, text="Forward",  command=move_forward).grid(row=1, sticky=N, column=2)
Button(root, text="Reverse", command=move_back).grid(row=3, sticky=S, column=2)
Button(root, text="Left", command=turn_left).grid(row=2, sticky=W, column=1)
Button(root, text="Snap", command=snap_pic).grid(row=2, column=2)
Button(root, text="Right", command=turn_right).grid(row=2, sticky=E, column=3)


