from gpiozero import Servo
from time import sleep

lock = Servo(17)
flag = Servo(18)

def hasMail():
    return True

def getMail():
    pass

def addMail():
    pass

def addMailList():
    pass

def lockDoor():
    lock.min()

def unlockDoor():
    lock.max()

def liftFlag():
    flag.max()

def lowerFlag():
    flag.min()
