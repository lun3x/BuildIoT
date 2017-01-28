class MailboxSim:

    def __init__(self):
        self.isDoorLocked = False
        self.isFlagDown = False

    def hasMail():
        print "hasMail"
        return True

    def getMail():
        print "getMail"
        return 0

    def addMail():
        print "addMail"
        if !isDoorLocked:
            print "addMail failed: door locked"
            return False
        else:
            return True

    def addMails(mails):
        print "addMails with " + mails
        if !isDoorLocked:
            print "addMails failed: door locked"
            return False
        else:
            return True;

    def lockDoor():
        print "lockDoor"
        if !isDoorLocked print "lockDoor: door already locked"
        isDoorLocked = True;

    def unlockDoor():
        print "unlockDoor"
        if isDoorLocked:
            print "unlockDoor: door unlocked"
            isDoorLocked = False
        else:
            print "unlockDoor: door already locked"

    def liftFlag():
        print "liftFlag"
        isFlagDown = False

    def lowerFlag():
        print "lowerFlag"
        isFlagDown = True
