# WASB-ot-: Twitter Bot for Game Development News
## Introduction
This is a Twitter bot that was created to help game developers stay up-to-date on the latest news and resources in the industry. The bot utilizes the Twitter API to post updates and the Beautiful Soup library to scrape news articles from various websites. Now supports multithreading and uses multiple websites for scraping. Also checks if previous tweets have been posted (this took a while!).

## Setup
To use this bot, you will need to have a Twitter account and apply for a Twitter Developer account to get an API key and secret. You will also need to have Python 3 and the following libraries installed:

`threading`

`Tweepy`

`requests`

`Beautiful Soup`


Once you have these, you can clone this repository and replace the placeholder values in the main.py file with your own API key and secret.

## Usage
The bot is designed to run on a schedule, posting updates at a set interval. You can adjust the interval and the websites to scrape for news articles in the scraper.py file.

The main.py file contains the main function of the bot, which handles the posting of updates to Twitter. To run the bot, you can use a task scheduler such as cron on Linux or Task Scheduler on Windows to run the script at the desired interval.

## Conclusion
This bot is a simple yet effective tool for game developers to stay informed on the latest happenings in the industry. Feel free to customize and expand upon the code to suit your specific needs. Happy coding!
