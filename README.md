This Jupyter Notebook analyzes a dataset of tweets about a Fast Moving Consumer Brand (FFCare). The goal is to assess brand engagement and sentiment.

# Objectives

Brand Mentions and Influencers

- Identify users with the highest number of tweets.

- Determine locations with the highest number of tweets.

- Identify sources with the highest number of tweets.

- Highlight tweets with the highest number of likes and retweets.

# Sentiment Analysis

- Analyze the overall sentiment of all tweets.

- Assess the sentiment of the tweets with the highest likes and retweets.

# Dataset

Columns: unique_id, tweet, date, username, location, source, num_of_likes, num_of_retweets

Preprocessing:

- Text cleaning, tokenization, stopword removal, and lemmatization.

- Extraction of week, month, and year from the tweet dates.

# Dependencies

The following Python libraries are required: torch, numpy, pandas, matplotlib, seaborn, nltk, textblob, wordcloud, Pillow, scipy, transformers, emot

# Preprocessing Steps

Data Cleaning:

- Convert text to lowercase.

- Remove special characters and numbers.

- Tokenize text and remove stopwords.

- Lemmatize words.

- Location Formatting:

- Normalize locations by removing special characters and converting to lowercase.

Date Features:

- Extract day of the week, week number, and year-month from tweet dates.

# Analysis

Brand Mentions and Influencers

Top Users:

- Bar chart of the top 20 users by the number of tweets.

Top Locations:

- Bar chart of the top 20 locations by the number of tweets.

Top Sources:

- Bar chart of the top 20 sources by the number of tweets.

Most Liked and Retweeted Tweets:

- Display tweets with the highest likes and retweets.

# Sentiment Analysis

Model Used: cardiffnlp/twitter-roberta-base-sentiment-latest

Steps:

- Tokenize tweets and pass them through the RoBERTa model.

- Compute sentiment scores (positive, negative, neutral) using softmax.

- Assign the sentiment with the highest score to each tweet.

# Findings:

- Analyzed 501 tweets from 320 unique users.
- Positive sentiment dominates (98.6%).
- SkinCareAddict is the top tweeter.
- Most tweets originate from Chicago, IL and Twitter web app.
- Tweets with high likes/retweets come from beard_buddy, Beard_expert, Beard_nation, chef_4_life, and beard_fan.
- Wednesdays see the most tweets.

# Recommendations:
- Maintain product quality based on positive sentiment.
- Address negative sentiment to improve brand image (e.g., Twitter Space discussions).
- Engage with high-influence users (beard_buddy, Beard_expert, etc.).
- Utilize Wednesdays for Twitter engagement and marketing campaigns.
