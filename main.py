from scraper import scraper
from threading import Thread
from tweeter import tweeting

# Create threads

scraper_thread = Thread(target=scraper)
main_thread = Thread(target=tweeting)

# Start threads
scraper_thread.start()
main_thread.start()

# Join threads
scraper_thread.join()
main_thread.join()
