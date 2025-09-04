import pandas as pd
import json

from run_prompt import execute_gemini_for_tweets

def top_5_selection(analyzed_tweets,engagement_type:str):
    df=pd.DataFrame(analyzed_tweets)
    filtered_df=df[df['engagement_type']==engagement_type]
    return filtered_df.nlargest(5,columns=['engagement_score']).to_dict(orient="records")

def create_tweet(analyzed_tweets):
    prompt = """
write a tweet for newly releasing
iphone 17 pro max with a18pro SoC launching
with physically moving camera zoom, 
make this tweet more for camera enthusiastic
audience 
    """
    engagement_type="like"
    
    top_5_tweets=top_5_selection(analyzed_tweets,engagement_type)
    
    system_prompt = f"""
    Create a engaging twitter tweet for my tech company
    PROMPT: {prompt}
    
    Here are some example tweets and their sentiment
    analysis with very high user
    engagements of other similar companies.
    Example Tweets: 
    {top_5_tweets}
    
    Create the tweet compare it with the example tweets
    and predict and explain why and how this tweet will
    perform well comparing to the given examples."""
    
    out=execute_gemini_for_tweets(prompt=system_prompt)
    
    try:
        out_dict=json.loads(out)
        tweet=out_dict['tweet']
        prediction=out_dict['prediction']
        explanation=out_dict['explanation']
        print("TWEET ========>")
        print(tweet)
        print("Prediction =======>")
        print(prediction)
        print("Explanation =======>")
        print(explanation)
        
    except Exception as e:
        print("Error parsing gemini output:",e)
        print("Raw Output",out)
        
with open("analyzed_tweets.json") as f:
    data = json.load(f)

# If data is a list of strings, convert each into a dict
if isinstance(data[0], str):
    data = [json.loads(item) for item in data]

print("tweets loaded ✅", len(data))
create_tweet(data)
