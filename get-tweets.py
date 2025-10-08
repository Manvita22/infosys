import json
import tweepy
from run_prompt import execute_gemini

from  constants import twitterClient


#http object used for interacting with twitter API


#user ID Extraction(user handle->user id)
user=twitterClient.get_user(username="sundarpichai")
print(user.data.id)
su_id=user.data.id

#using the user if we get the tweets
tweets=twitterClient.get_users_tweets(su_id,max_results=50,tweet_fields=['created_at','public_metrics','text'])

# print(tweets.data)

# for tweet in tweets.data:
#     print(tweet.text)
#     prompt=f"""Summarize the twitter tweet attached and give it a sentimental analysis score
#     TWEET=>{tweet.text}
#     """
#     llm_out=execute_gemini(prompt)
#     print(llm_out)
    
#save  the tweets to json file
with open("extracted_tweets.json", "w") as json_file:# output for analysis of tweets
    json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
