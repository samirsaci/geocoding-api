## Build Your Free GPS Routing API with Python Flask 🗺️
*Build your free Distance Matrix API deployed on the cloud*

### Article
In this [Article](https://www.samirsaci.com/build-a-gps-routing-api-with-python-flask/), we will create a free, easy-to-implement and customizable (and a bit slow :D) Distance Matrix API using Flask with a Selenium Bot deployed on Heroku

### How does it work?
Before you read this section, please forget everything you know about how to put in production fast, efficient, and stable code that guarantees quick response with limited resources.

This will be simple, quick, and dirty, with no intention of being a scalable solution. 

The performance will be way lower than if you directly query the official Google API — but here it’s free :)

[![This is an image](https://miro.medium.com/max/875/1*YqhaaI7ZuXfgAiGuuy166A.png)](https://www.samirsaci.com/build-a-gps-routing-api-with-python-flask/)

#### Let us do it in three steps
1. Build a Selenium Bot that will query the distance from City A to City B on the Google Maps website.
2. Set up your Flask API that will receive the request and return a distance
3. Deploy your code on Heroku

## Code
This repository code is ready to be deployed on Heroku:
##### 1. Clone the GitHub repository to your local folder and create a local Python environment
##### 2. Download libraries listed in requirements.txt
```
  pip3 install -r requirements.txt
```
##### 3. Download Buildpacks on Heroku to use Selenium + ChromeDriver
Go to settings > Add Buildpack
[![This is an image](https://miro.medium.com/max/875/1*mDsg_6F14SKeeds0kdHlwg.png)](https://www.samirsaci.com/build-a-gps-routing-api-with-python-flask/)
```
Enter Two Links
https://github.com/heroku/heroku-buildpack-google-chrome
https://github.com/heroku/heroku-buildpack-chromedriver
```
##### 4. Set up Environment Variables on Heroku
[![This is an image](https://miro.medium.com/max/875/1*2ENP1_ndBVoaSamUXUtVxw.png)](https://www.samirsaci.com/build-a-gps-routing-api-with-python-flask/)
```
CHROMEDRIVER_PATH: /app/.chromedriver/bin/chromedriver
GOOGLE_CHROME_BIN: /app/.apt/usr/bin/google-chrome
```
##### 5. Deploy your app on Heroku

## Test your API
#### Test your API to calculate the distance
```
From: Paris, France
To: Marseille, France
```

#### Request link
http://xxx-xxx.herokuapp.com/distance/Paris,France/Marseille,France
(replace xxx-xxx by your Heroku app name)

#### Response
{“distance”:”775 km”}

## About me 🤓
Senior Supply Chain Engineer with international experience working on Logistics and Transportation operations. \
Have a look at my portfolio: [Data Science for Supply Chain Portfolio](https://samirsaci.com) \
For **consulting or advising** on analytics and sustainable supply chain transformation, feel free to contact me via [Logigreen Consulting](https://www.logi-green.com/)
