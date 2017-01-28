try:
    from gpiozero import Servo
    from gpiozero import Button
except ImportError as e:
    from pi_sim import Servo
    from pi_sim import Button
from time import sleep

class MailboxPi:

    def __init__(self):
        self.lock = Servo(17)
        self.flag = Servo(18)
        self.floor = Button(6)
        self.door = Button(12)
        self.door.when_pressed = self._incrementMailCount
        self.floor.when_released = self._resetMailbox
        self.floor.when_pressed = self._liftFlag
        self.mailCount = 0

    def hasMail(self):
        return self.floor.is_pressed

    def getMailCount(self):
        return self.mailCount

    def lockDoor(self):
        self.lock.min()

    def unlockDoor(self):
        self.lock.max()

    def _liftFlag(self):
        self.flag.max()

    def _lowerFlag(self):
        self.flag.min()

    def _incrementMailCount(self):
        if self.floor.is_pressed:
            self.mailCount += 1

    def _resetMailbox(self):
        self.mailCount = 0
        self._lowerFlag()
