import os
import random
import tweepy

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

script_dir = os.path.dirname(os.path.realpath('__file__'))
definitions_path = "definitions.txt"
definitions_file = os.path.join(script_dir, definitions_path)

# Read definitions
definitions = open(definitions_file, "r")

def_list = []

for definition in definitions:
    def_list.append(definition)

# Randomly choose a definition
p = random.choice(def_list)
p2 = p.rstrip() 

# Create and expression to add at the end to make each tweet somewhat unique.
expressions = [" " + u'\U0001F602', '!', " " + u'\U0001F606', " " + u'\U0001F609']
expression = random.choice(expressions)

msg = f"The P stands for {p2}{expression}"

# Tweets what the P stands for
api.update_status(msg)

