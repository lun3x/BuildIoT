import tweepy
import json

from mailbox_pi import MailboxPi as Mailbox
from constants import *
from mention_stream_listener import MentionStreamListener

# Main
if __name__ == "__main__":
    # set up stream listener and stream
    mailbox = Mailbox()
    listener = MentionStreamListener(mailbox = mailbox)
    stream = tweepy.Stream(auth = api.auth, listener = listener)

    # start stream
    stream.filter(track = [mailboxHandle]) # the mailbox's handle
