# Sentiment-Analysis-using-Twitter-for-cryptocurrency
This is a Flask application that is used to get sentiments regarding a particular cryptocurrency in the realtime.These sentiments are derived from the tweets from the twitter.
In this we analyse the incoming tweets based on the hashtags and a combination of "Hashtags+influencers".

The Variable.py is the file that is holding all the required credentials which will be used later in the project.After replacing them with your own credentials,save it.
preprocess_data.py is the one responsible for cleaning up the incoming Tweets.This is implicitly called by one of the program later.

LSTM_new.py is the program containing the model, which is a LSTM model that is trained on clean.csv,and the model is saved(to fasten the process).
The training of the model is commented out(If required you can uncomment it and train it on any data you hold).Just change the parameters accordingly.

MySql is used as the database.Add the credentials in the Variable.py(the username and password to establish a database connection).
"tweets" is the database created and used(Create a database named tweets).This "tweets" database contains 2 tables.
hash_tweets table is used for storing the tweets based on the hashtags.
influ_tweets table is used to store the tweets based on hashtags and the influencers 
The columns that should present and named are as follows:
influ_tweets--->
 Date           | datetime     
 Tweets         | varchar(400)
 Category       | varchar(10) 
 Influencer     | varchar(40)
 
 has_tweets---->

Date            | datetime    
Tweets          | varchar(400) 
Category        | varchar(10)

Please make sure you use the same variable name!!

Hashtag_tweets.py is used to collect the tweets in realtime(based on hashtags only) and store them in the database(table hash_tweets).Run this python script (maybe in a console)
this file should be running infinitely,if you have to get the data over a span of time.

influencer_tweets.py used to collect the tweets in realtime(based on hashtags and influencers) and store them in the database(table influ_tweets).Run this python script (maybe in a console)
this file should be running infinitely,if you have to get the data over a span of time.

flask_influ.py --->This is the flask app used to get the sentiments based on hashtags only.It takes in the categ and ctype as a query argument
       categ --->bitcoin = "coin"
                 Etherium ="ether"
                 This is done so that you can get the tweets only related to a particular crypto you want to.If you want to include other crypt,just add the related hashtags in the Variable.py file.
       ctype ---->This is used to collect the tweets .Tells us whether to collect the data from the current time ,going backward in time in minutes or days.It also allows us to collect the data based on the date range
            for minutes--->pass the argument as [m no_of_minutes]
            for days ----->pass the argument as [d no_of_days]
            for a range of date--->pass the argument as [r %Y-%m-%d' %Y-%m-%d']   (the first date is the start date and the second one is the end date)

flask_hash.py---->This is the flask app used to get the sentiments based on hashtags and influencer.It takes in the categ and ctype as a query argument
       categ --->bitcoin = "coin"
                 Etherium ="ether"
                 This is done so that you can get the tweets only related to a particular crypto you want to.If you want to include other crypt,just add the related hashtags in the Variable.py file.
       ctype ---->This is used to collect the tweets .Tells us whether to collect the data from the current time ,going backward in time in minutes or days.It also allows us to collect the data based on the date range
            for minutes--->pass the argument as [m no_of_minutes]
            for days ----->pass the argument as [d no_of_days]
            for a range of date--->pass the argument as [r %Y-%m-%d  %Y-%m-%d]   (the first date is the start date and the second one is the end date)            



 