# Step 1: Download the Buildpacks Necessary for the ChromeDriver
# Buildpack 1: https://github.com/heroku/heroku-buildpack-google-chrome
# Buildpack 2: https://github.com/heroku/heroku-buildpack-chromedriver
# Step 2: Add the PATH variable to the Heroku configuration
# heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google_chrome
# heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get("https://medium.com")
print(driver.page_source)
print("Finished!")