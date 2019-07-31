#Variables that will have the user credentials to access the twitter API
ACCESS_TOKEN= "# Your Access Token"
ACCESS_TOKEN_SECRET="#Your Access Token Secret"
CONSUMER_KEY="#Your Consumer Key"
CONSUMER_SECRET="#Your Consumer Key Secret"

#Hashtags
coin_hash = ["#bitcoins" , "#btc" , "#bitcoin" , "#blockchain" , "#cryptocurrency" , "#bitcoinmining" , "#crypto" , "#bitcoinnews" ,"#btcusd"]
ether_hash = ['#etherium','#eth','#blockchain','$eth',	'#ethereumcoin','#ethereumprice','#ethereuminvestment','#ethereumgames','	#ethereumdeveloper']                             

#Influencers List
'''Procedure to upload the influencer list,Use the following commands
some_name= open(r"influencer.txt").readlines()   #Store the influencers in a text file named influencer.txt
#some_name = [i.strip() for i in influencers]
#joblib.dump(some_name,r'influencer_list.save')   #This approach fastens the process'''
            
coin_influ_list = 'influencer_list.save'              
ether_hash_list = 'ether_influencer_list.save'

#Credentials related to Mysql Database
user = '#Your Username'
password = '#Your Password'