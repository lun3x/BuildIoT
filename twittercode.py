import tweepy

auth = tweepy.OAuthHandler("1rapGRTeXdypArOAa10uxA1TS", "PxUathgqmHquKAFrKj2a4PAQXizGCogVUFy1eHKQI2SWrB1s5J")
auth.set_access_token("825312532302815232-0CNFh0KwJCthpAlRgpq2NeSXcycp2Pt", "Gs5tl2W1IVpCHpCTPvUp0w28ZwBCBw9Pji8onYmqeJhIQ")

api = tweepy.API(auth)

api.update_status('Hello World!')
