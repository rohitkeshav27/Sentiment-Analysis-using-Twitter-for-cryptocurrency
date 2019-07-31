import tweepy
import Variable
from urllib3.exceptions import ProtocolError
import http
import mysql.connector as mys
from dateutil import parser
from sklearn.externals import joblib
import random
mydb = mys.connect(host='localhost',user=Variable.user ,passwd = Variable.password)
mycursor = mydb.cursor()
mycursor.execute("use tweets") #This is the name of the Database
influencers = joblib.load(Variable.coin_influ_list) #This is the influencer list (Store them in the Variables.py)

if __name__ == '__main__':
    while True:
        try:
            # Initialize Stream listener
            hashtags = Variable.coin_hash
            categ = 'coin'    ###3Use 'coin' for Bitcoin and use 'ether' for Etherium
            #OUTPUT_FILE = "hashtags_json.txt"
            # Pass OAuth details to tweepy's OAuth handler
            auth = tweepy.OAuthHandler(Variable.CONSUMER_KEY, Variable.CONSUMER_SECRET)
            auth.set_access_token(Variable.ACCESS_TOKEN, Variable.ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth)
            influencers = joblib.load(Variable.coin_influ_list) #Choose the influencer list from Variable.py
            for i in influencers:
                try:
                    results = api.user_timeline(screen_name = i)
                    for tweet in results:
                        listo = tweet.text.split()
                        any1 = any(i in listo for i in hashtags)
                        if any1 is True:
                            tweet = tweet._json
                            name = tweet["user"]["name"]
                            dt = parser.parse(tweet["created_at"])
                            cat = dt.strftime("%Y-%m-%d, %H:%M:%S")
                            twet = str(tweet["text"])
                            sql = "INSERT INTO influ_tweets(Date,Tweets,Category,Influencer) VALUES (%s, %s,%s,%s)"
                            val = (cat, twet,categ,name)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            print(tweet["text"])
                                                        
                except Exception:
                        pass
                
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
                    pass
                except UnicodeDecodeError:
                    pass    
            
        finally:
            #if(mydb.is_connected()):
            #    mydb.close()
            #    print("MySQL connection is closed")
            random.shuffle(influencers)
            print("")

if(mydb.is_connected()):
            mydb.close()
            print("MySQL connection is closed")            