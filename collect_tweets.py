import json
from twython import Twython
import pandas as pd
import datetime


# Load credentials from json file
#with open("./twitter_credentials.json", "r") as file:  
    #creds = json.load(file)

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ{'CONSUMER_SECRET']
                          
    
# Instantiate an object
python_tweets = Twython(consumer_key, consumer_secret)

# Create query
query = {'q': 'united airlines',  
        'result_type': 'recent',
        'count': 100,
        'lang': 'en',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'location': [],'coordinates': []}  
for status in python_tweets.search(**query)['statuses']:  
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['coordinates'].append(status['coordinates'])
    dict_['location'].append(status['user']['location'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)  
current_date = datetime.datetime.now()
filename = str(current_date.day)+str(current_date.month)+str(current_date.year)
df.to_csv(str(filename + '.csv'))

#scraped_twitter.drop_duplicates(keep='first', inplace=True)

#scraped_twitter.to_csv("scraped_twitter.csv")
