# -*- coding: utf-8 -*-
"""Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uDAxcuSNIP04W7XAK9Uslc1drz3sauo4

## **Data Importing**

#### Scraping data
"""

!pip install git+https://github.com/JustAnotherArchivist/snscrape.git #Installing snscrape (data mining package)

import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_tweet(limit,query):
  """ 
  Download limit no. of tweets from twitter 
  with query and returns a dataframe
  """

  container = []

  for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(container) == limit:
        break
    else:
      if(tweet.lang == 'en'):
        container.append([tweet.user.username, tweet.date, tweet.rawContent])

  df = pd.DataFrame(container, columns=["User", "Date Created", "Tweet"])
  return df

limit = 10000
query = "Facebook since:2022-01-01 until:2022-11-01"
tweets_df = scrape_tweet(limit,query)
tweets_df.to_csv('Tweets_Before_Layoff.csv', index=False)

limit = 10000
query = "Facebook Layoffs since:2022-11-01 until:2023-04-01"
layoff_tweets_df = scrape_tweet(limit,query)
layoff_tweets_df.to_csv('Layoff_Tweets.csv', index=False)

limit = 10000
query = "Facebook since:2022-11-01 until:2023-04-01 exclude:retweets exclude:replies"
latest_tweets_df = scrape_tweet(limit,query)
latest_tweets_df.to_csv('Latest_Tweets2.csv', index=False)

limit = 100000
query = "Facebook since:2018-01-01 until:2023-04-01 exclude:retweets exclude:replies"
fb_training_df = scrape_tweet(limit,query)
fb_training_df.to_csv('fb_training_data.csv', index=False)

"""### Importing data"""

from google.colab import files
import io
import pandas as pd
 
""" 
Upload a CSV file from local device
and convert into a dataframe
"""
def upload():
  uploaded = files.upload()
  filename = next(iter(uploaded))
  df = pd.read_csv(io.BytesIO(uploaded[filename]),lineterminator='\n')
  return df

tweets_df = upload()
tweets_df.head()

"""## **Data Preprocessing**

### Importing Libraries
"""

## Data Manipulation 
import pandas as pd
import numpy as np

## Text Preprocessing
!pip install contractions
import contractions

import nltk
nltk.download('stopwords') #for stopwords
nltk.download('wordnet') #for WordNetLemmatizer
nltk.download('punkt') #for word_tokenize

import re
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

## Data Visualization 
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import style

## Machine Learning Libraries
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

import warnings
warnings.filterwarnings("ignore")

"""### Checking shape of dataframe

"""

tweets_df.shape

"""### Checking detailed information of dataframe"""

tweets_df.info()

"""### Checking for null values in dataframe"""

tweets_df.isnull().sum()

"""### Deleting unwanted columns"""

tweets_df.columns

tweets_df = tweets_df.drop(['User', 'Date Created'], axis=1)
tweets_df.head()

"""### Analyzing tweets before cleaning"""

print(tweets_df['Tweet'].iloc[0],"\n")
print(tweets_df['Tweet'].iloc[1],"\n")
print(tweets_df['Tweet'].iloc[2],"\n")
print(tweets_df['Tweet'].iloc[3],"\n")
print(tweets_df['Tweet'].iloc[4],"\n")
print(tweets_df['Tweet'].iloc[5],"\n")
print(tweets_df['Tweet'].iloc[9995],"\n")
print(tweets_df['Tweet'].iloc[9996],"\n")
print(tweets_df['Tweet'].iloc[9997],"\n")
print(tweets_df['Tweet'].iloc[9998],"\n")
print(tweets_df['Tweet'].iloc[9999],"\n")

"""### Data cleaning

1.   Lower casing
2.   Removal of Urls
3.   Removal of @tags and #
4.   Removal of punctuations
5.   Removal of emojis and symbols
6.   Removal of stop words
7.   Lemmatization





"""

def data_cleaning(tweet):
  # covert all text to lowercase
  tweet = tweet.lower()

  # remove all urls
  tweet = re.sub('http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)

  # remove @ user tags and #
  tweet = re.sub('\@\w+|\#', '', tweet)

  # remove emojis
  regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
                           "]+", flags = re.UNICODE)
  regrex_pattern.sub('',tweet)

  # remove numbers
  tweet = ''.join(c for c in tweet if not c.isdigit())

  # resolving contractions
  expanded = []
  for word in tweet.split():
    expanded.append(contractions.fix(word))
  tweet =  ' '.join(expanded)

  # remove punctuations
  tweet = re.sub('[^\w\s]', '', tweet)

  # remove stop words
  tweet_tokens = word_tokenize(tweet)
  filtered_texts = [word for word in tweet_tokens if word not in stop_words]

  # lemmatizing
  lemma = WordNetLemmatizer()
  lemma_texts = (lemma.lemmatize(text, pos='a') for text in filtered_texts)

  return " ".join(lemma_texts)

tweets_df.Tweet = tweets_df['Tweet'].apply(data_cleaning)

"""### Analyzing tweets after cleaning"""

print(tweets_df['Tweet'].iloc[0],"\n")
print(tweets_df['Tweet'].iloc[1],"\n")
print(tweets_df['Tweet'].iloc[2],"\n")
print(tweets_df['Tweet'].iloc[3],"\n")
print(tweets_df['Tweet'].iloc[4],"\n")
print(tweets_df['Tweet'].iloc[5],"\n")
print(tweets_df['Tweet'].iloc[9995],"\n")
print(tweets_df['Tweet'].iloc[9996],"\n")
print(tweets_df['Tweet'].iloc[9997],"\n")
print(tweets_df['Tweet'].iloc[9998],"\n")
print(tweets_df['Tweet'].iloc[9999],"\n")

"""### Checking for duplicate rows and deleting them"""

duplicate = tweets_df[tweets_df.duplicated()]
print(duplicate)

tweets_df = tweets_df.drop_duplicates('Tweet')

tweets_df.info()

"""### Calculating polarity"""

def polarity(Tweet):
  return TextBlob(Tweet).sentiment.polarity

tweets_df['Polarity'] = tweets_df['Tweet'].apply(polarity)
tweets_df.head(10)

"""### Labeling"""

def get_label(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

tweets_df['Sentiment'] = tweets_df['Polarity'].apply(get_label)
tweets_df.head()

"""### Saving the processed data"""

tweets_df.to_csv('Processed_tweets.csv',index=False)

"""### Plotting Word Cloud"""

words = ' '.join([tweets for tweets in tweets_df['Tweet']])
plt.figure(figsize = (20,15))
wordCloud = WordCloud(width = 1600, height = 800, random_state = 21).generate(words)
plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis("off")
plt.show()

"""#### Positive Tweets wordcloud"""

pos_tweets = tweets_df[tweets_df.Sentiment == 'Positive']
pos_tweets = pos_tweets.sort_values(['Polarity'], ascending = False)
pos_tweets.head()

pos_tweets.info()

words = ' '.join([tweets for tweets in pos_tweets['Tweet']])
plt.figure(figsize = (20,15))
wordCloud = WordCloud(width = 1600, height = 800).generate(words)
plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis("off")
plt.show()

"""#### Negative Tweets wordcloud"""

neg_tweets = tweets_df[tweets_df.Sentiment == 'Negative']
neg_tweets = neg_tweets.sort_values(['Polarity'], ascending = False)
neg_tweets.head()

words = ' '.join([tweets for tweets in neg_tweets['Tweet']])
plt.figure(figsize = (20,15))
wordCloud = WordCloud(width = 1600, height = 800).generate(words)
plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis("off")
plt.show()

"""## **Machine learning**

### Data splitting
"""

x_train, x_test, y_train, y_test = train_test_split(tweets_df["Tweet"], tweets_df["Sentiment"], test_size = 0.2, random_state = 50)

print(x_train,y_train)

"""### Feature extraction

#### Tfidf vectorizer
"""

vect = TfidfVectorizer(sublinear_tf=True).fit(x_train)

feature_names = vect.get_feature_names_out()
print("Number of features: {}\n".format(len(feature_names)))
print("First 50 features:\n {}".format(feature_names[:50]))

x_train = vect.transform(x_train)

"""### Linear Support Vector Classifier (SVM)"""

SVM_model = LinearSVC()
SVM_model.fit(x_train, y_train)

SVM_pred = SVM_model.predict(vect.transform(x_test))
SVM_accur = accuracy_score(SVM_pred, y_test)
print("Test accuracy: {:.2f}%".format(SVM_accur*100))

print(classification_report(y_test, SVM_pred))

style.use('classic')
conmat = confusion_matrix(y_test, SVM_pred, labels = np.unique(SVM_pred))
graph = ConfusionMatrixDisplay(confusion_matrix = conmat, display_labels = np.unique(SVM_pred))
graph.plot()

"""### Logistic Regression"""

LR_model = LogisticRegression()
LR_model.fit(x_train, y_train)

LR_pred = LR_model.predict(vect.transform(x_test))
LR_accur = accuracy_score(LR_pred, y_test)
print("Test accuracy: {:.2f}%".format(LR_accur*100))

print(classification_report(y_test, LR_pred))

style.use('classic')
conmat = confusion_matrix(y_test, LR_pred, labels = np.unique(LR_pred))
graph = ConfusionMatrixDisplay(confusion_matrix = conmat, display_labels = np.unique(LR_pred))
graph.plot()

"""### MultinomialNB (Naive Bayes)"""

NB_model = MultinomialNB()
NB_model.fit(x_train, y_train)

NB_pred = NB_model.predict(vect.transform(x_test))
NB_accur = accuracy_score(NB_pred, y_test)
print("Test accuracy: {:.2f}%".format(NB_accur*100))

print(classification_report(y_test, NB_pred))

style.use('classic')
conmat = confusion_matrix(y_test, NB_pred, labels = np.unique(NB_pred))
graph = ConfusionMatrixDisplay(confusion_matrix = conmat, display_labels = np.unique(NB_pred))
graph.plot()

"""### Comparing the accuracy of all models"""

style.use('ggplot')
models = ['LinearSVC (SVM)', 'Logistic Regression', 'MultinomialNB (Naive Bayes)']
values = np.array([SVM_accur,LR_accur,NB_accur])
accur = values*100
fig = plt.figure(figsize = (6, 6))
plt.bar(models, accur, color ='maroon', width = 0.3)
 
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Net Brand Reputation Comparisons")
plt.show()

"""### Saving the best performing model"""

import pickle
filename = 'final_trained_model.sav'
pickle.dump(SVM_model, open(filename, 'wb'))