# Measuring Effects of Layoffs on Company Reputation Using Sentiment Analysis
A research oriented project built with Python language in Google Collabs.

## Description of project
The project is titled ‘Measuring effects of layoffs on company reputation using sentiment analysis’. As the project title suggests, the primary focus of the project is on sentiment analysis of Twitter data. The analysis is then used to calculate the reputation of corporate entities. The ultimate goal of this product is to provide a comprehensive model that can be utilized to evaluate the reputation of a company based on data from Twitter. It also hopes to provide a moderate, but comprehensive expansion of the impact that events such as layoffs can have on a company’s reputation. It will describe how such events affect the way a company is perceived by the public and the potential consequences that may result. The product consists of all the components that are required for gathering data, cleaning data, analysing data, calculating results, and presenting it in a graphical format. This includes the process of scraping Twitter, natural language processing, and machine learning, and then visualizing the results using charts and plots that can be easily comprehended. The aforementioned products not only assist in comprehending human opinions on different topics but also enable businesses to utilize this analysis to devise effective strategies for their growth and success. The product relies on a machine learning (ML) model that has been trained more than100,000 tweets of span of 5 years, resulting in an impressive accuracy rate of 94%. This indicates the high success rates of the machine learning model and its ability to give accurate results. Moreover, the users have the flexibility to download specific data fragments and modify the model according to their preferences. This feature empowers the users to evaluate and calculate different types of reputation scores for the company. They can experiment with different models to evaluate a wide range of factors that may affect a company's reputation such as its financial strength, market position, customer satisfaction, and so on. By retraining the model with different data segments, users can get a better understanding of the reputation status of the company. One of the significant advantages of running this project is that you don't need any special software to run it smoothly. The project is developed on Google Colab, which is an online platform designed for NLP and ML, among others. The project can be readily uploaded to the platform and used right away.

## Flowchart (overview of project)
![image](https://github.com/Sam-cudo/Comapany-Reputation-Using-Sentiment-Analysis/assets/54752818/dcb4ece4-2487-4457-9738-4bbf772e95d1)

## Components of project
The whole project is divided in three notebooks:
### 1. Data mining from twitter
In this notebook we use Snscape to scrape the tweets and create different datasets.
![image](https://github.com/Sam-cudo/Comapany-Reputation-Using-Sentiment-Analysis/assets/54752818/d59da414-4d2c-42a8-8717-da1314373b97)

### 2. Choosing a model and training it
Here we clean the training data and after performing basic data preprocessing we train three machine learning models(SVM, logistic regresssion, Naive baiyes) and compare them to find the most accurate.

### 3. Predicting the sentiment and calculating the corporate reputation
Here we use the pre-trained model to predict the sentiments and use a formula to calculate company reputation from diffrent datasets and then analyse them with help of graphs.
