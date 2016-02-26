from gpiozero import Motor
import picamera
from time import sleep
from tkinter import *

root = Tk()
root.wm_title("RaspiBot")
motor1 = Motor(17)
motor2 = Motor(24)
motor3 = Motor(23)
motor4 = Motor(27)
i = 0
camera = picamera.PiCamera()
myFile = "/home/pi/BotPics/raspiCam.jpg"


def turn_right():
    motor1.on()
    motor2.on()
    sleep(.18)
    motor1.off()
    motor2.off()

def turn_left():
    motor3.on()
    motor4.on()
    sleep(.18)
    motor3.off()
    motor4.off()

def move_forward():
    motor1.on()
    motor3.on()
    sleep(1)
    motor1.off()
    motor3.off()

def move_back():
    motor2.on()
    motor4.on()
    sleep(1)
    motor2.off()
    motor4.off()

def snap_pic():
    camera.capture(myFile)

Label(text="Raspi Remote").grid(row=0, column=2, sticky=N)
Button(root, text="Forward",  command=move_forward).grid(row=1, sticky=N, column=2)
Button(root, text="Reverse", command=move_back).grid(row=3, sticky=S, column=2)
Button(root, text="Left", command=turn_left).grid(row=2, sticky=W, column=1)
Button(root, text="Snap", command=snap_pic).grid(row=2, column=2)
Button(root, text="Right", command=turn_right).grid(row=2, sticky=E, column=3)


