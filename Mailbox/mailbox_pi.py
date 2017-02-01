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
        # get refernces to GPIO pins
        self.lock = Servo(17)
        self.flag = Servo(18)
        self.floor = Button(6)

        # set inital values of flag down, door locked
        self.flag.min()
        self.lock.value = -0.2

        # set event handlers for raising and lowering the flag
        self.floor.when_released = self._lowerFlag
        self.floor.when_pressed = self._liftFlag

    def hasMail(self):
        return self.floor.is_pressed # true or false

    def lockDoor(self):
        self.lock.value = -0.2

    def unlockDoor(self):
        self.lock.value = -1

    def _liftFlag(self):
        print("You've got mail")
        self.flag.mid() # raise flag
        api.update_status("You've got mail! -- {0}".format(time.strftime('%X %x'))) # tweet confirmation

    def _lowerFlag(self):
        print("You've emptied your mail")
        self.flag.min() # lower flag
        api.update_status("You've emptied your mail -- {0}".format(time.strftime('%X %x'))) # tweet confirmation
