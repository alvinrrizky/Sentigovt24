import time
import tweepy
from sentiment.models import Tweet

def crawl_tweet(input_query):
    access_token = "3221004481-HdKucoOhc3D8vtVHHhzx6r39wBM5k9Il5CHm7bI"
    access_token_secret = "4LWYCLTcngX2M6fBznA9w88FDLZGR1rA4lcbKXmgdX6GX"
    api_key = "XjAWG9nyEJ4d88bvRkC8phix9"
    api_key_secret = "xSmszxt2ZDoEJ27mVzYiHKmeA3XCB1YZjPYAIJYjfXIHEKiLbS"

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    crawlTweets = []

    for tweet in tweepy.Cursor(api.search_tweets,q=input_query,count=15,lang="id").items():
        tweets = {
            'tweet_id':tweet.id,
            'created_at':tweet.created_at,
            'user_name':tweet.user.screen_name,
            'text':tweet.text.encode("utf-8"),
        }
        crawlTweets.append(tweets)
    

    return crawlTweets

class MyStreamListener(tweepy.Stream):
    
    def __init__(self, time_limit=300):
        self.start_time = time.time()
        self.limit = time_limit
        super(MyStreamListener, self).__init__()
    
    def on_connect(self):
        print("Connected to Twitter API.")
        
    def on_status(self, status):
        
        res = {}
        # Tweet ID
        tweet_id = status.id
        
        # User ID
        user_id = status.user.id
        # Username
        username = status.user.name
        
        
        # Tweet
        if status.truncated == True:
            tweet = status.extended_tweet['full_text']
            hashtags = status.extended_tweet['entities']['hashtags']
        else:
            tweet = status.text
            hashtags = status.entities['hashtags']
        
        # Read hastags
        # hashtags = read_hashtags(hashtags)            
        
        # Retweet count
        # retweet_count = status.retweet_count
        # Language
        lang = status.lang
        
        print(status.text)
        # If tweet is not a retweet and tweet is in English
        # if not hasattr(status, "retweeted_status") and lang=="id":
            # Connect to database
            # dbConnect(user_id, username, tweet_id, tweet, retweet_count, hashtags)
            # tweet = {
            # 'tweet_id':status.id,
            # # 'created_at':status.created_at,
            # 'user_name':status.user.screen_name,
            # 'text':status.text.encode("utf-8"),
            # }
            # res.append(tweet)
            # Tweet.objects.bulk_create(res)
            
            
        if (time.time() - self.start_time) > self.limit:
            
            print(time.time(), self.start_time, self.limit)
            return False
            
    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_data disconnects the stream
            return False