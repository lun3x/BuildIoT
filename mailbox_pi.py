from gpiozero import Servo
from gpiozero import Button
from time import sleep
from mailbox_sim import MailboxSim

class MailboxPi(MailboxSim):

    # static class attributes
    lock = Servo(17)
    flag = Servo(18)
    floor = Button(6)
    door = Button(12)

    def __init__(self):
        super(MailboxPi, self).__init__()
        door.when_pressed = _incrementMailCount
        floor.when_released = _resetMailCount
        floor.when_pressed = _liftFlag
        
    def hasMail(self):
        super(MailboxPi, self).hasMail()
        return floor.is_pressed

    def getMailCount(self):
        return super(MailboxPi, self).getMail()

    def lockDoor(self):
        lock.min()
        return super(MailboxPi, self).lockDoor()

    def unlockDoor(self):
        lock.max()
        return super(MailboxPi, self).unlockDoor()

    def _liftFlag(self):
        flag.max()
        return super(MailboxPi, self)._liftFlag()

    def _lowerFlag(self):
        flag.min()
        return super(MailboxPi, self)._lowerFlag()
        
    def _incrementMailCount(self):
        if floor.is_pressed:
            super(MailboxPi, self)._incrementMailCount()
        
    def _resetMailCount(self):
        super(MailboxPi, self)._resetMailCount()
