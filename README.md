# You'veGotMailBox

##Building an Internet of Things mailbox in 24 hours

This is the code behind the physical mailbox we built for the Bristol Electrical and Electronics Engineering Society. Here's the thing itself:

![The finished mailbox itself](https://lh3.googleusercontent.com/baL2eCiW3-LWrMa_eZ1ih3BbEbh6ixd77PlQHdwtkhZBb3_0NL8vVsVmk-3PIM0n7fNVo4gTyHvue1b6tiLnToWz_jQ33FBcrI9drDXqjdLoZxTcVHcgAGfVvTMCW7bd7XITeZk=w751-h1334-no)

There are two servos inside, one which raises and lowers the red flag, and one which moves some internal grabber arms around the bolt attached to the door, locking it if it's closed.

It has a twitter account: [@you'vegotmailbox](https://twitter.com/youvegotmailbox) where it will look through any tweets mentioning it, check if they contain any of the following commands, and respond appropriately.

It maintains an internal whitelist of users to accept commands from, it will not accept commands from other users and will reply to any unauthorised commands with "Sorry, you are not authorised to use this mailbox".

```
lock             - locks the door and replies to confirm
unlock           - unlocks the door and replies to confirm
mail             - replies with whether there is mail inside the box
whitelist <user> - adds <user> to list of authorised users
blacklist <user> - removes <user> from list of authorised users
```

When mail is pushed through the slot it will tweet "You've got mail!" with a link to a Youtube video of the AOL "You've got mail!" notification.

When mail is removed from the box it will tweet "You've emptied your mailbox".
