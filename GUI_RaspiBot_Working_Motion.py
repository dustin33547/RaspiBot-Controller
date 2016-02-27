from gpiozero import Motor
import picamera
from time import sleep
from tkinter import *

root = Tk()
root.wm_title("RaspiBot")
motor1 = Motor(forward=17, reverse=23)
motor2 = Motor(forward=24, reverse=27)
i = 0
camera = picamera.PiCamera()
myFile = "/home/pi/BotPics/raspiCam.jpg"


def turn_right():
    motor1.forward()
    motor2.reverse()
    sleep(.18)
    motor1.off()
    motor2.off()

def turn_left():
    motor1.reverse()
    motor2.forward()
    sleep(.18)
    motor1.off()
    motor2.off()

def move_forward():
    motor1.forward()
    motor2.forward()
    sleep(1)
    motor1.off()
    motor2.off()

def move_back():
    motor1.reverse()
    motor2.reverse()
    sleep(1)
    motor1.off()
    motor2.off()

def snap_pic():
    camera.capture(myFile)

Label(text="Raspi Remote").grid(row=0, column=2, sticky=N)
Button(root, text="Forward",  command=move_forward).grid(row=1, sticky=N, column=2)
Button(root, text="Reverse", command=move_back).grid(row=3, sticky=S, column=2)
Button(root, text="Left", command=turn_left).grid(row=2, sticky=W, column=1)
Button(root, text="Snap", command=snap_pic).grid(row=2, column=2)
Button(root, text="Right", command=turn_right).grid(row=2, sticky=E, column=3)


