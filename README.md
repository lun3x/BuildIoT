# You'veGotMailBox

## An Internet of Things mailbox built in 24 hours

This is the code behind the physical mailbox we built for the Bristol Electrical and Electronics Engineering Society. Here's the thing itself:

![The finished mailbox itself](https://lh3.googleusercontent.com/JBOLk2kRuas3IXMAvmMjfrTWjYjIg7DdXKFgnGj5vd_4b1ocJDp2dm7yfOuWZGATze-9c8vzpX4ok2olP2xucIM8AaDA7hUEflK9CfdkDkpnqHHI8J8GzSgBA0pOgZ7q9pMIdPRnKQSzU1ekk8V0gguhswrJ3fwUkYvqPs0Rs8qi49FAUDQVX86aEFc_WJC2SIfxAR01WQ7RwQhvXQMg-wKShvxMFgfElRBorr6qP58QdRFf51K5Ytz7sX8kRb4uDAo622j7DGx8zd1bK3GtU8gsK3mGVgpcjhguz2wOMr2xNvIIThRZDVA7kFUK2eZkCYVL6LMH-MQ2KA_haGvHH7RzXBJ-45VvF3hbhb5KFKJdoAmnHFAFxjujQi8pXSh0ADNS2_JBtO_z7Xj39MDn4oZGVftMUj9wgAzkS59lA0W_tXi1KgPSojOSYqkzSeXTZwH6y4VDH7MLc8L_9kqVDFUNJWsTsuY0TyzVZPpJ5NQUoa6aLnqKNKDlLdkmvdadj07WJBFygoWxsiaR3SzXtg_n4VMGMIM9_kGeol43bFTwaMf_R8IHA2LyhpQO-ThH1BVsht8JqCLLCWspe8Sk_yXik-TOJbU7NS2qDYYpFGo5PubO0SntuUcTlb40mNrDlk5OLSFNtlI3VaPQEEyt7pBbI4j5Q-xB-IsQFpyaQsg=w1255-h1334-no)

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
