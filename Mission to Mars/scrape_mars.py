
# coding: utf-8

# # Mission to Mars Homework 12 - VCHU

# # Step 1- Scraping
# NASA Mars News
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd
from localenv import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)
import tweepy
import time



def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser=init_browser()
    mars_datadict={}
    Nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(Nasa_url)
    Nasa_html = browser.html
    Nasa_soup=bs(Nasa_html, 'html.parser')

    latest_article = Nasa_soup.find('div', class_='list_text')
    article_par = latest_article.find('div', class_='article_teaser_body').text
    article_title = latest_article.find('div', class_='content_title').text

    mars_datadict["article_title"] = article_title
    mars_datadict["article_par"] = article_par

    #print(article_title)
    #print(article_par)


# # JPL Mars Space Images - Featured Image
    JPL_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(JPL_url)
    JPL_html = browser.html
    JPL_soup = bs(JPL_html, 'html.parser')
    JPL_img = JPL_soup.find('a', 'fancybox')['data-fancybox-href']
    JPL_url = "https://www.jpl.nasa.gov"+JPL_img
    featured_image_url = JPL_url
    
    mars_datadict["featured_image_url"] = featured_image_url

    #print(featured_image_url)


# # Mars Weather

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    target_user = "MarsWxReport"
    latest_tweet = api.user_timeline(target_user, count=1)
    mars_weathertweet=latest_tweet[0]['text']

    mars_datadict["mars_weathertweet"] = mars_weathertweet


    #mars_weathertweet


# # Mars Facts

    Mars_url = "http://space-facts.com/mars/"
    tables = pd.read_html(Mars_url)

    Mars_df = tables[0]
    Mars_df
    html_table = Mars_df.to_html()
    html_table

    mars_datadict["html_table"] = html_table

# # Mars Hemisphere 

    Hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(Hemisphere_url)
    Hemisphere_html = browser.html
    Hemisphere_soup = bs(Hemisphere_html, 'html.parser')
    hemisphere_data=[]
    for i in range(4):
        mars_img = browser.find_by_tag('h3')
        mars_img[i].click()
        Hemisphere_html=browser.html
        Hemisphere_soup=bs(Hemisphere_html, 'html.parser')
        mars_imgurl=Hemisphere_soup.find("img", class_="wide-image")["src"]
        image_title = Hemisphere_soup.find("h2", class_="title").text
        image_url = 'https://astrogeology.usgs.gov' + mars_imgurl
        info={"image title":image_title,
                "image url":image_url}
        hemisphere_data.append(info)
        browser.back()

    mars_datadict["hemisphere_data"] = hemisphere_data
    hemisphere_data
    return mars_datadict
    mars_datadict
# # Step 2 - MongoDB and Flask Application
