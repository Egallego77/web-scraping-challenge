


# Import Splinter, BeautifulSoup, and Pandas

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pymongo
import requests
import pathlib
import pprint

def scrape_all():

    # Path to chromedriver


    path = "/usr/local/bin/chromedriver"


    # Set the executable path and initialize the chrome browser in splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    # browser = Browser('chrome', **executable_path, headless=True)



    browser = Browser('chrome', **executable_path, headless=True)

    ## Visit the NASA mars news site

    # Visit the mars nasa news site
    nasa_url = 'https://mars.nasa.gov/news/'


    # Optional delay for loading the page
    browser.visit(nasa_url)


    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')




    # .find() the content title and save it as `news_title`
    news_titles = soup.find_all('div', class_='content_title')
    news_title = news_titles[1].text

    # .find() the paragraph text
    soup.find('div', class_='article_teaser_body').text

    ## JPL Space Images Featured Image

    # Visit JPL space images Mars URL 

    jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'

    browser.visit(jpl_url)


    # Parse the resulting html with soup

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup




    soup.find('img', 'headerimage fade-in')



    # find the relative image url
    img_src = soup.find('img', 'headerimage fade-in')['src']
    img_src

    # Use the base url to create an absolute url
    featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_src}'
    featured_image_url

    ## Mars Facts

    # Create a dataframe from the space-facts.com mars page

    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    df = tables[1]


    # clean the dataframe and export to HTML

    to_html = df.to_html()
    html_table = to_html.replace('\n', '')
    html_table

    ## Hemispheres

    # visit the USGS astrogeology page for hemisphere data from Mars

    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    soup



    # First, get a list of all of the hemispheres
    hemisphere = soup.find('h3')



    # Next, loop through those links, click the link, find the sample anchor, return the href
        
    hemispheres = soup.find_all('h3')
    titles = []
    for hemisphere in hemispheres:
        titles.append(hemisphere.text)
        
        
        # We have to find the elements on each loop to avoid a stale element exception
        
        
        # Next, we find the Sample image anchor tag and extract the href
        
        
        # Get Hemisphere title
        
    titles = sorted(titles)
    imgs = soup.find_all('a', class_='itemLink product-item')
    planets = []
    for img in imgs:
        planets.append(img['href'].split('/')[-1])
    planets = sorted(list(set(planets)))
    planets

    results = []
    for title, planet in zip(titles,planets):
        document = {'img_url': f'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/{planet}.tif/full.jpg',
    'title': title
        } 
        results.append(document)

    mars_data = {"data": results}

    # view the hemisphere urls to make sure they look good
    return mars_data
