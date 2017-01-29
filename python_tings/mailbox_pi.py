try:
    from gpiozero import Servo
    from gpiozero import Button
except ImportError as e:
    from pi_sim import Servo
    from pi_sim import Button
import time
from constants import *

class MailboxPi:

    def __init__(self):
        self.lock = Servo(17)
        self.flag = Servo(18)
        self.flag.min()
        self.lock.value = -0.2
        self.floor = Button(6)
        self.floor.when_released = self._lowerFlag
        self.floor.when_pressed = self._liftFlag
        self.mailInBox = False

    def hasMail(self):
        return self.floor.is_pressed

    def lockDoor(self):
        self.lock.value = -0.2

    def unlockDoor(self):
        self.lock.value = -1

    def _liftFlag(self):
        print("You've got mail")
        api.update_status("You've got mail! -- {0}".format(time.strftime('%X %x')))
        self.flag.mid()

    def _lowerFlag(self):
        print("You've emptied your mail")
        api.update_status("You've emptied your mail -- {0}".format(time.strftime('%X %x')))
        self.flag.min()
