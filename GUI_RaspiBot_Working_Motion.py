from gpiozero import Motor
import picamera
from time import sleep
from tkinter import *
from random import randint

root = Tk()
motor1 = Motor(17, 24)
motor2 = Motor(23, 27)
i = 0
camera = picamera.PiCamera()
myFile1 = "pic.gif"


def turn_right():
    motor2.forward()
    motor1.backward()
    sleep(.18)
    motor1.stop()
    motor2.stop()

def turn_left():
    motor2.backward()
    motor1.forward()
    sleep(.18)
    motor1.stop()
    motor2.stop()

def move_forward():
    motor1.forward()
    motor2.forward()
    sleep(.25)
    motor1.stop()
    motor2.stop()

def move_back():
    motor1.backward()
    motor2.backward()
    sleep(.25)
    motor1.stop()
    motor2.stop()

def snap_pic(): 
    camera.capture(myFile1)

def myPic():
    photo = PhotoImage(file="pic.gif")
    w = Label(root, image=photo)
    w.photo = photo
    w.grid(row=1, column=4)

Label(text="Raspi Remote").grid(row=0, column=2, sticky=N)

Button(root, text="Forward",  command=move_forward).grid(row=2, column=2)
Button(root, text="Left", command=turn_left).grid(row=3, column=1)
Button(root, text="Snap", command=snap_pic).grid(row=3, column=2)
Button(root, text="Right", command=turn_right).grid(row=3, column=3)
Button(root, text="Load Pic", command=myPic).grid(row=4, column=2)
Button(root, text="Reverse", command=move_back).grid(row=5, column=2)
