from flask import Flask, request,render_template,make_response
from flask_restful import Resource, Api
import Variable
import datetime
import preprocess_data
import LSTM_new
#from matplotlib import pyplot as plt
import mysql.connector as mys


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        args = request.args
        categ = args.get('categ',type= str)
        ctype = args.get('ctype',type = str)
        #categ = 'coin'
        #ctype = 'd 1'
        dates = str(ctype).split()
        if dates[0] == 'm':                   #If the arguments are passed in minutes
            now = datetime.datetime.now()
            second = int(dates[1])*60
            new = now - datetime.timedelta(seconds=second)
        if dates[0] == 'd':                  #If the arguments are passed in days
            now = datetime.datetime.now()
            second = int(dates[1])*86400
            new = now - datetime.timedelta(seconds=second)
        if dates[0] == 'r':                 #If the arguments are passed as a range of date
            now = datetime.strptime(dates[2], '%Y-%m-%d')
            new = datetime.strptime(dates[1], '%Y-%m-%d')
        mydb = mys.connect(host='localhost',user=Variable.user ,passwd = Variable.password)
        
        mycursor = mydb.cursor()
        
        mycursor.execute("use tweets")  #The name of the database
        
        sentiments = []
        try:
            sql_select_query = "select Tweets from hash_tweets where Date >= %s and Date <= %s and Category = %s"
            mycursor.execute(sql_select_query, (new,now,categ))
            records = [preprocess_data.preprocess_tweet(str(i)) for i in mycursor]
            sentiments = [LSTM_new.predict(i)['label'] for i in records]            
            if sentiments.count(1) > sentiments.count(0):
                check = float(sentiments.count(1)/len(sentiments))
                if check >= 0.45 and check <= 0.55:
                    tag = 'Neutral'
                else:
                    tag='Positive'
            else:
                if float(sentiments.count(0)/len(sentiments)) >= 0.45 and float(sentiments.count(0)/len(sentiments)) <= 0.55:
                    tag = 'Neutral'
                else:
                    tag='Negative'
            res = {"Positive":sentiments.count(1) , "Negative" : sentiments.count(0) , "Overall" : tag}        
            final=dict(zip(records,sentiments))
            res.update(final)
            final = res
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('result.html' , result = final),headers)
        finally:
            
            #closing database connection.
            '''if(mydb.is_connected()):
                mydb.close()
                print("MySQL connection is closed")'''
            
            

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)