# Step 1: Download the Buildpacks Necessary for the ChromeDriver
# Buildpack 1: https://github.com/heroku/heroku-buildpack-google-chrome
# Buildpack 2: https://github.com/heroku/heroku-buildpack-chromedriver
# Step 2: Add the PATH variable to the Heroku configuration
# heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google_chrome
# heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver
# heroku ps:scale worker=0 
from selenium import webdriver
from bs4 import BeautifulSoup as soup 
import os
import time

# Chromedrive setting
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Link
link = "https://medium.com"
fr = 'Paris, France'
to = 'Marseille, France'

# url
url = 'https://www.google.fr/maps/dir/{}/{}/data=!4m2!4m1!3e0'.format(fr, to)
# url = 'https://www.google.fr/maps/dir/Paris/Marseille/@45.988302,-0.6461436,6z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x47e66e1f06e2b70f:0x40b82c3688c9460!2m2!1d2.3522219!2d48.856614!1m5!1m1!1s0x12c9bf4344da5333:0x40819a5fd970220!2m2!1d5.36978!2d43.296482!3e0'
# Driver get
driver.get(url)
time.sleep(3)
# Get pagesoup
page_soup = soup(driver.page_source, "html.parser")
print(page_soup)
# Extract
css_dist = "div[class^='section-directions-trip-distance'] > div"
try:
    distance = page_soup.select_one(css_dist).text
except Exception as e:
    print(e)
    distance = 'Error'

print("{} to {}: {}".format(fr, to, distance))
print("Finished!")