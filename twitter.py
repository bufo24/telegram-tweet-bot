from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def tweet(message):
    try:
        twitter.update_status(status=message)
        return True
    except Exception as e:
        raise Exception(e)