# %%
sentence_1 = "i had a great time at the movie it was really funny"
sentence_2 = "i had a great time at the movie but the parking was terrible"
sentence_3 = "i had a great time at the movie but the parking wasn't great"
sentence_4 = "i went to see a movie"

# %%
from textblob import TextBlob

sentiment_score = TextBlob(sentence_1)
print(sentiment_score.sentiment.polarity)

# %%
sentiment_score_2 = TextBlob(sentence_2)
print(sentiment_score_2.sentiment.polarity)

# %%
sentiment_score_3 = TextBlob(sentence_3)
print(sentiment_score_3.sentiment.polarity)

# %%
sentiment_score_4 = TextBlob(sentence_4)
print(sentiment_score_4.sentiment.polarity)

# %%
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

vader_sentiment = SentimentIntensityAnalyzer()
print(vader_sentiment.polarity_scores(sentence_1))

# %%
print(vader_sentiment.polarity_scores(sentence_2))

# %%
print(vader_sentiment.polarity_scores(sentence_3))

# %%
print(vader_sentiment.polarity_scores(sentence_4))

# %%
