# Import Tweepy and Pandas Libraries.
# Install first if necessary.
import tweepy as tw
import pandas as pd

# Use your own Twitter.com Developer Keys inside the double-quotes
consumer_key = "Tk...."
consumer_secret = "AO...."
access_token = "55...."
access_token_secret = "y0...."

# Authenticate with Twitter - nothing to change here since it uses the variables above
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Declare what you want search_words to look for. Here I'm using Twitter's PlaceID for Windsor
search_variable = "place:15b0a643e7bd22c7 since:2019-06-01"

# Uncomment to filter out ReTweets. I am interested in RT's so will comment out
twitter_search = search_variable #+ " -filter:retweets"

# Collect tweets in tweets variable. Will attempt to collect no more than 50 tweets, change it to your requirment.
tweets = tw.Cursor(api.search,
              q=twitter_search,
              lang="en",).items(50)
              
# Iterate and print the information you are looking for in each collected tweet
for tweet in tweets:
    tweet_data = [[tweet.place, tweet.retweet_count, tweet.favorite_count, tweet.coordinates, tweet.user.created_at, tweet.user.screen_name, tweet.user.location, tweet.user.statuses_count, tweet.user.followers_count, tweet.user.verified, tweet.created_at] for tweet in tweets]

# Put the collected data tweet_text into Pandas DF for writing to table
tweet_text = pd.DataFrame(data=tweet_data, 
                          columns=['Place', 'RetweetCount', '# Faves Count', 'Coordinates', 'Join Date', 'user', "location", 'Tweets', 'followers', 'verified', 'tweeteddate'])

# Check on work in the Console. Uncomment to see tweets collected.
# print(tweet_text)

# This is a nifty Pandas tool to write out to an Excel file with a custom sheet name
tweet_text.to_excel("TwitterInfluence.xlsx", sheet_name="WindsorTwitter") 

