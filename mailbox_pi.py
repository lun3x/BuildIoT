from gpiozero import Servo
from time import sleep
from mailbox_sim import MailboxSim

class MailboxPi(MailboxSim):

    # static class attributes
    lock = Servo(17)
    flag = Servo(18)

    def __init__(self):
        super(MailboxPi, self).__init__()

    def hasMail():
        print("Checked for mail")
        return super(MailboxPi, self).hasMail()

    def getMail():
        return super(MailboxPi, self).getMail()

    def addMail():
        return super(MailboxPi, self).addMail()

    def addMails(mails):
        return super(MailboxPi, self).addMails(mails)

    def lockDoor():
        lock.min()
        return super(MailboxPi, self).lockDoor()

    def unlockDoor():
        lock.max()
        return super(MailboxPi, self).unlockDoor()

    def liftFlag():
        flag.max()
        return super(MailboxPi, self).liftFlag()

    def lowerFlag():
        flag.min()
        return super(MailboxPi, self).lowerFlag()
