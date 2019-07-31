import tweepy
import Variable
from urllib3.exceptions import ProtocolError
import http
import mysql.connector as mys

from dateutil import parser


mydb = mys.connect(host='localhost',user=Variable.user ,passwd = Variable.password)

mycursor = mydb.cursor()

mycursor.execute("use tweets") #The database name given is tweets
# Use the required one from Variable.py (Add extra hashtags with another name and use it here)
hashtags = Variable.coin_hash   #This is used for Hastags of Bitcoin (Can change accordingly)
categ = 'coin'    ###3Use 'coin' for Bitcoin and use 'ether' for Etherium
class MyStreamListener(tweepy.StreamListener):
    """
    Twitter listener, collects streaming tweets and output to a file
    """
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        tweet = status._json
        dt = parser.parse(tweet["created_at"])
        cat = dt.strftime("%Y-%m-%d, %H:%M:%S")
        twet = str(tweet["text"])
        sql = "INSERT INTO hash_tweets(Date,Tweets,Category) VALUES (%s, %s , %s)"
        val = (cat, twet , categ)
        mycursor.execute(sql, val)
        mydb.commit()
        print(tweet["text"])      
        return True
    def on_exception(self, exception):
        pass
           
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':
    # Initialize Stream listener
    # Pass OAuth details to tweepy's OAuth handler
    auth = tweepy.OAuthHandler(Variable.CONSUMER_KEY, Variable.CONSUMER_SECRET)
    auth.set_access_token(Variable.ACCESS_TOKEN, Variable.ACCESS_TOKEN_SECRET)
    l = MyStreamListener()
    # Create you Stream object with authentication
    try:
        stream = tweepy.Stream(auth, l)
        # Filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hashtags , languages = ["en"])    
    except tweepy.TweepError as e:
        print("Tweepy Error is: ", e.reason)
        pass
    except http.client.IncompleteRead as e:
        print("http exception is: ", e)
        pass
    except UnicodeEncodeError as e:
        print("Unicode error is: ", e)
        pass
    except ProtocolError as e:
        print("url exception is:", e)
        #time.sleep(35)
        pass
    except UnicodeDecodeError:
        pass    
    
    finally:
        #closing database connection.
        if(mydb.is_connected()):
            mydb.close()
            print("MySQL connection is closed")