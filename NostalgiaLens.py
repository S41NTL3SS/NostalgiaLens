import pandas as pd
import tweepy
import praw
import requests
from googleapiclient.discovery import build
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# Twitter API Configuration from  https://developer.x.com/en
twitter_bearer_token = 'YOUR twitter bearer token' 

# Reddit API Configuration from https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fprefs%2Fapps&rdt=53257
reddit_client_id = 'YOUR reddit client id'
reddit_client_secret = 'YOUR reddit client secret'
reddit_user_agent = 'YOUR user agent'

# Facebook API Configuration from https://developers.facebook.com/
facebook_access_token = 'facebook access token'
facebook_group_id = 'TARGET_GROUP_OR_PAGE_ID'  # ANY Public group/page ID

# YouTube API Configuration from https://console.cloud.google.com/welcome/new?pli=1
youtube_api_key = 'YT api key'
youtube_search_query = 'nostalgia millennials'


def fetch_twitter_data(query="nostalgia OR 'I miss' OR 'wish I could go back'", max_results=100):
    client = tweepy.Client(bearer_token=twitter_bearer_token)
    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    twitter_data = [{"text": tweet.text, "created_at": tweet.created_at, "user_id": tweet.author_id} for tweet in tweets.data]
    return pd.DataFrame(twitter_data)

def fetch_reddit_data(subreddit="nostalgia", limit=100):
    reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)
    posts = reddit.subreddit(subreddit).top(limit=limit)
    reddit_data = [{"text": post.title + " " + post.selftext, "created_at": post.created_utc, "user_id": post.author} for post in posts]
    return pd.DataFrame(reddit_data)

def fetch_facebook_data():
    url = f"https://graph.facebook.com/v11.0/{facebook_group_id}/feed"
    params = {
        "access_token": facebook_access_token,
        "fields": "message,created_time,id"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        facebook_data = response.json()['data']
        return pd.DataFrame(facebook_data)
    else:
        print("Error fetching Facebook data:", response.json())
        return pd.DataFrame()

def fetch_youtube_data(max_results=50):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    request = youtube.search().list(
        q=youtube_search_query,
        part="snippet",
        maxResults=max_results,
        type="video"
    )
    response = request.execute()
    youtube_data = [{"text": item['snippet']['title'] + " " + item['snippet']['description'], "created_at": item['snippet']['publishedAt'], "user_id": item['id']['videoId']} for item in response['items']]
    return pd.DataFrame(youtube_data)

def analyze_sentiment(data):
    sentiment_scores = []
    for item in data['text']:
        analysis = TextBlob(item)
        sentiment_scores.append(analysis.sentiment.polarity)
    data['sentiment'] = sentiment_scores
    return data

def extract_keywords(data):
    keywords = []
    for text in data['text']:
        keywords.extend(text.lower().split())
    keyword_counts = Counter(keywords)
    return keyword_counts

def create_wordcloud(keyword_counts):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(keyword_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Common Nostalgic Keywords")
    plt.show()

def plot_sentiment(data):
    plt.hist(data['sentiment'], bins=5, edgecolor="black")
    plt.title("Sentiment Distribution of Nostalgic Posts")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.show()

def main():
    twitter_data = fetch_twitter_data()
    reddit_data = fetch_reddit_data()
    facebook_data = fetch_facebook_data()
    youtube_data = fetch_youtube_data()
    
    combined_data = pd.concat([twitter_data, reddit_data, facebook_data, youtube_data], ignore_index=True)
    
    analyzed_data = analyze_sentiment(combined_data)
    
    keyword_counts = extract_keywords(analyzed_data)
    
    create_wordcloud(keyword_counts)
    plot_sentiment(analyzed_data)
    
    print("Sentiment Analysis Results:\n", analyzed_data[['text', 'sentiment']])
    print("\nTop Keywords:\n", keyword_counts.most_common(10))

if __name__ == "__main__":
    main()
