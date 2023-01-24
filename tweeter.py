import tweepy
import time
from scraper import tips_and_resources


def tweeting():

    consumer_key = "Ns11du5d94nkPUhAGRe8wgjow"
    consumer_secret = "x6eJ9UbGGpJMaB34oscMJHVEkRpvo6eHNy3LYMtny4caaZMU5y"
    access_token = "3165048462-AybyEBO46WVsLaoEwzrahrXjoq2zu0vampZ2Z0t"
    access_token_secret = "QdZm8cuv41lTY51UUsDgbK6Hi2KYhYGVrO9qvCgzJjeXv"

    # Authenticate with Twitter API
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name="nerdisland1728")

    tweeted = set()  # Create a set to store previously tweeted articles

    for tweet in tweets:
        tweeted.add(tweet.text)

    while True:
        for item in tips_and_resources:
            tweet_exists = False
            # Check if the current tweet has already been posted
            if item['title'].strip() in tweeted:
                print("Duplicate, so skipping.\n")
                continue

            if not tweet_exists:  # If tweet hasn't been tweeted, tweet it
                try:
                    api.update_status(item["title"] + "\n" + item["link"])
                    time.sleep(3600)
                except tweepy.errors.TweepyException as e:  # Exception handling
                    if e == 187:
                        print("Duplicate tweet.\n")
                        continue
                    else:
                        continue
