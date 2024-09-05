import streamlit as st
import pandas as pd
from textblob import TextBlob

# Set the layout to wide
st.set_page_config(layout="wide")

# Load the dataset
df = pd.read_csv('C:/Users/DELL/Documents/github/banthony_projects/sentiment_analysis/tweets_2.csv', encoding="latin1")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Extract month and day of the week from the date column
df['month'] = df['date'].dt.strftime('%B')
df['day_of_week'] = df['date'].dt.strftime('%A')

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["FFCare Tweets Dashboard", "Analyse a Tweet"])

# Dashboard Page
if page == "FFCare Tweets Dashboard":
    st.title("Twitter Analytics Dashboard")

    # 1. Track Brand Mentions and Identify Influencers
    st.header("Track Brand Mentions and Identify Influencers")

    col1, col2 = st.columns(2)

    # a. Users with the highest number of tweets
    with col1:
        st.subheader("Top Users by Tweet Count")
        top_users = df['username'].value_counts().head(10)
        st.bar_chart(top_users)

    # b. Location with the highest number of tweets
    with col2:
        st.subheader("Top Locations by Tweet Count")
        top_locations = df['location'].value_counts().head(10)
        st.bar_chart(top_locations)

    col3, col4 = st.columns(2)

    # c. Source with the highest number of tweets
    with col3:
        st.subheader("Top Sources by Tweet Count")
        top_sources = df['source'].value_counts().head(10)
        st.bar_chart(top_sources)

    # d. Tweets with the highest number of likes and retweets
    with col4:
        st.subheader("Tweets with the Most Engagement")
        top_tweets = df[['username', 'tweet', 'num_of_likes', 'num_of_retweets']].sort_values(
            by=['num_of_likes', 'num_of_retweets'], ascending=False).head(10)
        st.write(top_tweets)



    col5, col6 = st.columns(2)
    # a. Tweets by month
    with col5:
        st.subheader("Tweets by Month")
        tweets_by_month = df['month'].value_counts().reindex(
            ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        ).fillna(0)
        st.bar_chart(tweets_by_month)
        # st.line_chart(tweets_by_month)


    # b. Tweets by day of the week
    with col6:
        st.subheader("Tweets by Day of the Week")
        tweets_by_day = df['day_of_week'].value_counts().reindex(
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        ).fillna(0)
        st.bar_chart(tweets_by_day)


    # 3. Measure Opinions
    st.header("Measure Opinions")

    # a. Overall sentiment of all tweets
    st.subheader("Overall Sentiment of Tweets")
    df['sentiment'] = df['tweet'].apply(lambda x: TextBlob(x).sentiment.polarity)
    overall_sentiment = df['sentiment'].mean()
    st.write(f"Overall Sentiment: {'Positive' if overall_sentiment > 0 else 'Negative' if overall_sentiment < 0 else 'Neutral'}")

    # b. Sentiment of the tweet with the highest likes and retweets
    st.subheader("Sentiment of Top Tweet")
    top_tweet = df.loc[df[['num_of_likes', 'num_of_retweets']].sum(axis=1).idxmax()]
    top_tweet_sentiment = TextBlob(top_tweet['tweet']).sentiment.polarity
    st.write(f"Tweet: {top_tweet['tweet']}")
    st.write(f"Sentiment: {'Positive' if top_tweet_sentiment > 0 else 'Negative' if top_tweet_sentiment < 0 else 'Neutral'}")


# Tweet Sentiment Analysis Page
elif page == "Analyse a Tweet":
    st.title("Tweet Sentiment Analysis")

    user_tweet = st.text_area("Paste the tweet here:")

    if st.button("Analyze Sentiment"):
        if user_tweet:
            sentiment = TextBlob(user_tweet).sentiment.polarity
            st.write(f"Sentiment: {'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'}")
        else:
            st.write("Please paste a tweet to analyze.")
