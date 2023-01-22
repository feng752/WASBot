import tweepy
import time
from scraper import tips_and_resources

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler("cosumer-key", "consumer-secret", "access-token", "access-token-secret")
api = tweepy.API(auth)

# Post a new tip or resource every hour
while True:
    for tip_or_resource in tips_and_resources:
        api.update_status(tip_or_resource)
        time.sleep(3600)
