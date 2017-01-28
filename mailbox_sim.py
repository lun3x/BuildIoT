class MailboxSim:

    def __init__(self):
        self.isDoorLocked = False
        self.isFlagDown = False
        self.mailCount = 0

    def hasMail(self):
        print "hasMail"

    def getMailCount(self):
        print "getMail"
        return self.mailCount

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
        
    def _incrementMailCount(self):
        print "incrementMailCount"
        self.mailCount += 1
        
    def _resetMailCount(self):
        print "resetMailCount"
        self.mailCount = 0
        self._lowerFlag()
