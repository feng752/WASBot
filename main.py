import tweepy
import time
from scraper import tips_and_resources

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler("Ns11du5d94nkPUhAGRe8wgjow", "x6eJ9UbGGpJMaB34oscMJHVEkRpvo6eHNy3LYMtny4caaZMU5y", "3165048462-ROimi1pdhC0cVAtD7wtqFxYPq82srQVibFHjmz4", "0uadAxUpPqhqadw9vlNeDAvh7QXwJwFbWjbD4bBqfkHo4")
api = tweepy.API(auth)

# Post a new tip or resource every hour
while True:
    for tip_or_resource in tips_and_resources:
        api.update_status(tip_or_resource)
        time.sleep(3600)
