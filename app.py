import os
import time
from flask import Flask, render_template, request, redirect
from selenium import webdriver
from bs4 import BeautifulSoup as soup 

# Chromedrive setting
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Link
fr = 'Paris, France'
to = 'Marseille, France'

app = Flask(__name__)

def from_to(fr, to):
    # url
    url = 'https://www.google.fr/maps/dir/{}/{}/data=!4m2!4m1!3e0'.format(fr, to)
    print("link: {}".format(url))
    # Driver get
    driver.get(url)
    time.sleep(1)
    # Soupify
    page_soup = soup(driver.page_source, "html.parser")
    # Extract
    css_dist = "div[class^='section-directions-trip-distance'] > div"
    css_dura = "div[class^='section-directions-trip-duration']"
    
    try:
        distance = page_soup.select_one(css_dist).text
        duration = page_soup.select_one(css_dura).text
    except Exception as e:
        print(e)
        distance = 'Error'
        duration = 'Error'
    print("{} to {}: {}".format(fr, to, distance))
    result = {
        "distance": distance
        # "distance": distance, 
        # "duration": duration
        }

    return result

# Routing do define url
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/distance/<fr>/<to>', methods=['GET', 'POST'])
def distance(fr, to):
  #returns the post, the post_id should be an int
  result = from_to(fr, to)
  return result


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, port=5000)