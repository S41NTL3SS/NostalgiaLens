NostalgiaLens is a Python tool designed to capture and analyze nostalgic trends across generations by collecting data from social media platforms like Twitter, Reddit, Facebook, and YouTube. This tool provides insights into the themes, eras, and cultural elements that resonate with each generation, making it valuable for researchers, marketers, and content creators.

#Features

  - Cross-Platform Analysis: Gathers nostalgic data from Twitter, Reddit, Facebook, and YouTube.

  - Sentiment Analysis: Uses sentiment scores to categorize nostalgic sentiments as positive, neutral, or negative.

  - Keyword Extraction & Visualization: Generates word clouds and keyword frequency lists to highlight common nostalgic topics.

  - Insightful Visuals: Provides sentiment distribution charts and keyword visualizations for easy trend analysis.

(Setup Instructions)

1. Clone the Repository
   *git clone https://github.com/your-username/NostalgiaLens.git*

1.2 Navigate into the project folder
    *cd NostalgiaLens*

3. Install the required libraries by running:
   *pip install -r requirements.txt*

4. Setup API KEYS
  This project requires API keys for each platform. You can store these as environment variables or add them to a .env file.

    Twitter: TWITTER_BEARER_TOKEN
    Reddit: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
    Facebook: FACEBOOK_ACCESS_TOKEN, FACEBOOK_GROUP_ID
    YouTube: YOUTUBE_API_KEY

For security, never share your API keys publicly.

4.Usage
  Run the main script to start data collection and analysis:
    *python nostalgia_analysis.py*

  Example Output
    Sentiment Analysis Results: Displays sentiment scores for each post, indicating the general tone of nostalgia.
    
    Keyword Cloud and Sentiment Distribution: Generates visuals to showcase common nostalgic topics and their associated         sentiments.
 

5. Dependencies
  pandas, tweepy, praw, requests, google-api-python-client, textblob, wordcloud, matplotlib

These dependencies can be installed via *pip install -r requirements.txt.*

License
This project is licensed under the MIT License.

