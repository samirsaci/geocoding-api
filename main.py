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
url = 'https://www.google.com/maps/dir/{}/{}'.format(fr, to)
# Driver get
driver.get(url)
# Get pagesoup
page_soup = soup(driver.page_source, "html.parser")
# Extract
css_dist = "div[class^='section-directions-trip-distance'] > div"
try:
    distance = page_soup.select_one(css_dist).text
except Exception as e:
    print(e)
    distance = 'Error'

print("{} to {}: {}".format(fr, to, distance))
print("Finished!")