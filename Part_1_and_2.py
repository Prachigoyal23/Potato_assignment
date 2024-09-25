import pandas as pd

# Load the data
df_small = pd.read_csv('path_to_large_file.tsv', sep='\t', low_memory=False)

# Filter relevant columns
columns = ['created_at', 'id', 'text', 'like_count', 'place_id']
df = df_small[columns]

# Query Functionality
# Here, we’ll define functions to query the data as per your requirements.

from datetime import datetime

def query_tweets(term):
    # Filter tweets containing the term
    filtered_tweets = df[df['tweet_text'].str.contains(term, case=False)]
    
    # Query 1: Tweets per day
    tweets_per_day = filtered_tweets['created_at'].dt.date.value_counts()
    
    # Query 2: Unique users
    unique_users = filtered_tweets['user_id'].nunique()
    
    # Query 3: Average likes
    average_likes = filtered_tweets['likes'].mean()
    
    # Query 4: Place IDs
    place_ids = filtered_tweets['place_id'].value_counts()
    
    # Query 5: Times of day
    filtered_tweets['time_of_day'] = filtered_tweets['created_at'].dt.hour
    tweets_per_hour = filtered_tweets['time_of_day'].value_counts()
    
    # Query 6: Most tweets by a user
    most_tweets_user = filtered_tweets['user_id'].value_counts().idxmax()
    
    return {
        'tweets_per_day': tweets_per_day,
        'unique_users': unique_users,
        'average_likes': average_likes,
        'place_ids': place_ids,
        'tweets_per_hour': tweets_per_hour,
        'most_tweets_user': most_tweets_user
    }

