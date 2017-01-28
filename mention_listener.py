import tweepy
import mailbox

#override tweepy.StreamListener to add logic to on_status
class MentionStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        mentionedScreenname = next((mention_screen_name for mention in status.entities.user_mentions if mention.screen_name == 'youvegotmailbox'), None)

        # if mentioned the bot, do what they asked
        if mentionedScreenname != None:
            text = status.text
            sn = status.user.screen_name

            if "do i have mail" in text.lower():
                self._replyMailInfo(status, sn)
            elif "lock my mailbox" in text.lower():
                self._lockMailBox(status, sn)
            elif "unlock my mailbox" in text.lower():
                self._unlockMailBox(status, sn)
            else:
                self._unrecognisedCommand(status, sn)


    def on_error(self, status_code):
        '''disconnect stream if too many api calls
        '''
        if status_code == 420:
            return False


    def _replyMailInfo(self, status, sn):
        tweet = "@{0} You have {1} unread mail".format(sn, len(mailbox.getMail))
        api.update_status(tweet, status.id)


    def _lockMailBox(self, status, sn):
        mailbox.lockDoor()
        tweet = "@{0} We have locked your mailbox :)"
        api.update_status(tweet, status.id)



# Main
if __name__ == "__main__":
    # set up API
    auth = tweepy.OAuthHandler("1rapGRTeXdypArOAa10uxA1TS", "PxUathgqmHquKAFrKj2a4PAQXizGCogVUFy1eHKQI2SWrB1s5J")
    auth.set_access_token("825312532302815232-0CNFh0KwJCthpAlRgpq2NeSXcycp2Pt", "Gs5tl2W1IVpCHpCTPvUp0w28ZwBCBw9Pji8onYmqeJhIQ")
    api = tweepy.API(auth)

    # set up stream listener and stream
    listener = MentionStreamListener()
    stream = tweepy.Stream(auth = api.auth, listener = listener)

    # start stream
    stream.filter(track = ['youvegotmailbox']) # our handle
