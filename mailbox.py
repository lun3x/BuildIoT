from gpiozero import Servo
from time import sleep

lock = Servo(17)
flag = Servo(18)

def hasMail():
    print("Checked for mail")
    return True

def getMail():
    pass

def addMail():
    pass

def addMailList():
    pass

def lockDoor():
    print("Locking door")
    lock.min()

def unlockDoor():
    print("Unlocking door")
    lock.max()

def liftFlag():
    print("Lifting flag")
    flag.max()

def lowerFlag():
    print("Lowering flag")
    flag.min()
