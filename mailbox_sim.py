class MailboxSim:

    def __init__(self):
        self.isDoorLocked = False
        self.isFlagDown = False
        self.mailCount = 0

    def hasMail(self):
        print "hasMail"
        if self.mailCount > 0:
            return True
        else:
            return False

    def getMailCount(self):
        print "getMail"
        return self.mailCount

    def addMail(self):
        print "addMail"
        if self.isDoorLocked:
            print "addMail failed: door locked"
            self.mailCount += 1
            return False
        else:
            return True

    def addMails(self, mails):
        print "addMails with " + mails
        if self.isDoorLocked:
            print "addMails failed: door locked"
            return False
        else:
            return True

    def popMail(self):
        print "popMail"
        if self.isDoorLocked:
            print "popMail failed: door locked"
            return False
        else:
            self.mailCount -= 1
            return True

    def lockDoor(self):
        print "lockDoor"
        if self.isDoorLocked:
             print "lockDoor: door already locked"
        self.isDoorLocked = True

    def unlockDoor(self):
        print "unlockDoor"
        if self.isDoorLocked:
            self.isDoorLocked = False
        else:
            print "unlockDoor: door already unlocked"

    def _liftFlag(self):
        print "liftFlag"
        self.isFlagDown = False

    def _lowerFlag(self):
        print "lowerFlag"
        self.isFlagDown = True
