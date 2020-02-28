
import tweepy                                                #basic importing of dependencies
from textblob import TextBlob

cons_key='muC2S2jyQCx6P5LYM73Tius5i'                                   #consumer encryption and decryption
cons_secret='dbA03Dc6hDDCAETZzuwrXjIaQbmsBxUQfnPaAABr9xXfDflYG1'

access_token='2523586407-aoyLWwQL1CaNOyRUFnGhtkzO284BoVsyB7Deqpn'      #to access the acc
acess_token_secret='jTMZXxB04EOKRsWe4axnjmzVeN1NFZs9Xwv8gY3Rjff4T'

auth = tweepy.OAuthHandler(cons_key,cons_secret)                                #function to authenticate the consumer
auth.set_access_token(access_token,acess_token_secret)                        #get tob twitter and authenticate the access token

print("enter count")

api = tweepy.API(auth) #from tweepy the API method that takes a single authentication argument

public_tweets = api.search(q='Trump', count=input()) # gets/retrieve the tweets that contain the word trump and stores em here

with open("files.csv",'w') as file1:   #opening / creating the file names files.csv
	for tweet in public_tweets:         #loop to move throught the individual tweets
		analysis=TextBlob(tweet.text)   #capturing tweets using textblob as "text"
		new_list=list(analysis)         #converting the textblob tuple to a list for easy access
		file1.write("\n")               
		for x in new_list:               #loop to traverse through the list of new analysis value
 
		     file1.write(x)              #writing down the values to the csv file 
		     

print("Executed successfully")
