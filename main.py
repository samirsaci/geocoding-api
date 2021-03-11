# Step 1: Download the Buildpacks Necessary for the ChromeDriver
# heroku buildpacks:add --index 1 https://github.com/heroku-buildpack-chromedriver
# heroku buildpacks:add --index 2 https://github.com/heroku-buildpack-chromedriver
# Step 2: Add the PATH variable to the Heroku configuration
# heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google_chrome
# heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver
from selenium import webdriver
import os

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH
browser = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
browser.get("https://medium.com")

print(browser.page_source)
print("Finished!")