import tweepy
import json
rasppi = False #mailbox: use prints or rasp pi actions
if rasppi:
    from mailbox_pi import MailboxPi as Mailbox
else:
    from mailbox_sim import MailboxSim as Mailbox

# constants
handle = 'youvegotmailbox'

#override tweepy.StreamListener to add logic to on_status
class MentionStreamListener(tweepy.StreamListener):

    def __init__(self, mailbox):
        self.mailbox = mailbox
        super(MentionStreamListener, self).__init__()

    def on_status(self, status):
        # get tweet json
        tweetdata = status._json

        # get first user dict whose screen_name is `handle`
        mentionedScreenname = next((mention['screen_name'] for mention in tweetdata['entities']['user_mentions'] if mention['screen_name'] == handle), None)

        # if tweeter mentioned the bot, do what they asked
        if mentionedScreenname != None:
            text = status.text
            sn = str(status.user.screen_name)

            if "do i have mail" in text.lower():
                self._replyMailInfo(status, sn)
            elif "lock" in text.lower():
                self._lockMailBox(status, sn)
            elif "unlock" in text.lower():
                self._unlockMailBox(status, sn)
            else:
                self._unrecognisedCommand(status, sn)


    def on_error(self, status_code):
        '''disconnect stream if too many api calls'''
        if status_code == 420:
            return False
        else:
			return True


    # private

    def _replyMailInfo(self, status, sn):
        text = '@{0} You have {1} unread mail'.format(sn, mailbox.getMailCount())
        api.update_status(text, status.id)

    def _lockMailBox(self, status, sn):
        print "got here"
        mailbox.lockDoor()
        print "got here"
        text = '@{0} We have locked your mailbox :)'.format(sn)
        api.update_status(text, status.id)

    def _unlockMailBox(self, status, sn):
        mailbox.unlockDoor()
        text = '@{0} We have unlocked your mailbox :)'.format(sn)
        api.update_status(text, status.id)

    def _unrecognisedCommand(self, status, sn):
        text = '@{0} Sorry, we do not recognise that command :('.format(sn)
        api.update_status(text, status.id)



# Main
if __name__ == "__main__":
    # set up API
    auth = tweepy.OAuthHandler("1rapGRTeXdypArOAa10uxA1TS", "PxUathgqmHquKAFrKj2a4PAQXizGCogVUFy1eHKQI2SWrB1s5J")
    auth.set_access_token("825312532302815232-0CNFh0KwJCthpAlRgpq2NeSXcycp2Pt", "Gs5tl2W1IVpCHpCTPvUp0w28ZwBCBw9Pji8onYmqeJhIQ")
    api = tweepy.API(auth)

    # set up stream listener and stream
    mailbox = Mailbox()
    listener = MentionStreamListener(mailbox)
    stream = tweepy.Stream(auth = api.auth, listener = listener)

    # start stream
    stream.filter(track = [handle]) # our handle
