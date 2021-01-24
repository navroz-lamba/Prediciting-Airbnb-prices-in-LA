# Airbnb prices in LA

Predicts the nightly rates of Airbnb in Los Angeles depending on the location, property type, number of bedrooms, etc.

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-Plotly_Dash-green)
![Library](https://img.shields.io/badge/Library-pandas-yellow)
![Library](https://img.shields.io/badge/ML_Library-scikit_learn-purple)
![Library](https://img.shields.io/badge/NLP_Library-NLTK-lightblue)
![PaaS](https://img.shields.io/badge/Paas-Heroku-fcba03)

## Overview of the project

•	Performed Data Wrangling and Exploratory Data Analysis to process 126 features in the dataset 

•	Dataset was found to be highly skewed and it was fixed by filtering out the outliers

•	Created new columns using feature engineering for better model performance

•	Used NLTK as NLP library to extract the information from amenities column 

•	Created a model using Random Forest Regressor as a predictor that precisely predicted the price of an Airbnb listing

•	Model was hyper tuned using Randomized Search CV

•	Used Mean Absolute Error as the evaluation metric considering the outliers in the dataset 

•	Joblib library was used to pickle the model and to load it in Flask 

•	Plotly Dash was used as the front-end 

•	The web application was deployed on Heroku


## Check out the application:
https://airbnb-la.herokuapp.com/

## Check out the blog for an end-to-end project along with explanation and solutions to some of the problems I ran into:
https://medium.com/analytics-vidhya/predicting-airbnb-prices-in-los-angeles-14758afc47e

## Quick demo: 

![ezgif com-gif-maker](https://user-images.githubusercontent.com/67918990/101460122-2b5cfa00-3907-11eb-8892-3adb0edd9d50.gif)

## How to run the project?

• Install all the dependencies in the procfile.lock 

• Clone this repository in your local system

• Open the command prompt from your project directory and run the command 'python run.py'

• Go to your browser and type http://127.0.0.1:5000/ in the address bar

• ALL SET! 

Source of the dataset : http://insideairbnb.com/get-the-data.html

## NOTE - 

• I have added the notebook if you would further like to understand the code better, or maybe look at data wrangling and EDA. 
