import time
import datetime
import pytz
import snscrape.modules.twitter as sntwitter
from .preprocessing import TextPreprocessing
from sentiment.helpers.sentiment_helper import predict, orderLabel
from bacapres.models import Bacapres
from sentiment.models import Tweet

until_time = int(time.time())
since_time = until_time - 300
print(since_time, " ", until_time)

dt_utc = datetime.datetime.utcnow()
timezone = pytz.timezone('Asia/Jakarta')

def scrape():
    print("start scrape")
    preprocessor = TextPreprocessing()
    data = scrape_tweet()

    data = preprocessor.removeIrrelevantTweet(data)
    result = []
    i = 1

    for i in range(0, len(data)):
        preprocessed_text = preprocessor.getFinalPreprocessingResult(data[i]['text'])
        sentiment = predict(preprocessed_text)

        bacapres = Bacapres.objects.get(id=data[i]['bacapres'])

        obj_tweet = Tweet(
            tweet_id = data[i]['tweet_id'],
            text = data[i]['text'],
            text_preprocessed = preprocessed_text,
            created_at = data[i]['created_at'],
            user_name = data[i]['user_name'],
            sentiment = orderLabel(sentiment),
            bacapres = bacapres
        )
        print(i)
        i=i+1
        result.append(obj_tweet)
    Tweet.objects.bulk_create(result)

def scrape_tweet():
    tweets = []
    bacapres = Bacapres.objects.all()
    i = 1

    for query in bacapres:
        print(query.name)
        for tweet in sntwitter.TwitterSearchScraper(query.name+f" since_time:{since_time} until_time:{until_time} lang:id").get_items():
            tweet_date = tweet.date
            tweet_id = str(tweet.id)
            data = {
            'tweet_id':tweet_id,
            'created_at':tweet_date.replace(tzinfo=pytz.utc).astimezone(timezone),
            'user_name':tweet.user.username,
            'text':tweet.content,
            'bacapres':query.id,
            'keyword':query.name,
            }
            print(i)
            i=i+1
            tweets.append(data)

    return tweets