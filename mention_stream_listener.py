import tweepy
import json

from constants import *

#override tweepy.StreamListener to add logic to on_status
class MentionStreamListener(tweepy.StreamListener):

    def __init__(self, mailbox):
        self.mailbox = mailbox
        super(MentionStreamListener, self).__init__()

    def on_status(self, status):
        # get tweet json
        tweetdata = status._json

        # get first user dict whose screen_name is `handle`
        mentionedScreenname = next((mention['screen_name'] for mention in tweetdata['entities']['user_mentions'] if mention['screen_name'] == mailboxHandle), None)

        # if tweeter mentioned the bot, do what they asked
        if mentionedScreenname != None:
            # get tweet text and user info
            text = status.text
            sn = str(status.user.screen_name)

            # validate user is authorised to make tweet commands
            try:
                print sn
                self._authUser(status)
            except Exception as e:
                self._userAuthError(status)
                return # end method

            # respond to request
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


    # private

    def _replyMailInfo(self, status, sn):
        text = '@{0} You have {1} unread mail'.format(sn, self.mailbox.getMailCount())
        api.update_status(text, status.id)

    def _lockMailBox(self, status, sn):
        self.mailbox.lockDoor()
        text = '@{0} We have locked your mailbox :)'.format(sn)
        api.update_status(text, status.id)

    def _unlockMailBox(self, status, sn):
        self.mailbox.unlockDoor()
        text = '@{0} We have unlocked your mailbox :)'.format(sn)
        api.update_status(text, status.id)

    def _unrecognisedCommand(self, status, sn):
        text = '@{0} Sorry, we do not recognise that command :('.format(sn)
        api.update_status(text, status.id)


    def _authUser(self, status):
        sn = status.user.screen_name
        print sn
        if not sn in whitelistUsers:
            raise Exception

    def _userAuthError(self, status):
        sn = status.user.screen_name
        text = '@{0} Sorry, you are not authorised to use this mailbox. :/'.format(sn)
        api.update_status(text, status.id)
