class MailboxSim:

    def __init__(self):
        self.isDoorLocked = False
        self.isFlagDown = False
        self.mailCount = 0

    def hasMail():
        print "hasMail"
        if mailCount > 0:
            return True
        else:
            return False

    def getMailCount():
        print "getMail"
        return mailCount

    def addMail():
        print "addMail"
        if isDoorLocked:
            print "addMail failed: door locked"
            mailCount += 1
            return False
        else:
            return True

    def addMails(mails):
        print "addMails with " + mails
        if isDoorLocked:
            print "addMails failed: door locked"
            return False
        else:
            return True

    def popMail():
        print "popMail"
        if isDoorLocked:
            print "popMail failed: door locked"
            return False
        else:
            mailCount -= 1
            return True

    def lockDoor():
        print "lockDoor"
        if isDoorLocked:
             print "lockDoor: door already locked"
        isDoorLocked = True;

    def unlockDoor():
        print "unlockDoor"
        if isDoorLocked
            isDoorLocked = False
        else:
            print "unlockDoor: door already unlocked"

    def _liftFlag():
        print "liftFlag"
        isFlagDown = False

    def _lowerFlag():
        print "lowerFlag"
        isFlagDown = True
