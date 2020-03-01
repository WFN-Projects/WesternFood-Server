# BEFORE RUNNING THIS FILE, GO INTO PRIVATE.PY AND ENTER YOUR CREDENTIALS FOR UWO LOGIN
# this file logs into the website and scrapes + creates list of transactions

from scraper.scrape import scrapeFile
from selenium import webdriver
import platform
# from private import *

def get_scraped_data(login_user, login_pass):
    ## UWO LOGIN TO CAMPUS MEAL PLAN
    if platform.system() == 'Linux':
        browser = webdriver.Chrome("chromedriver")
    elif platform.system() == 'Windows':
        browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://mealplan.uwo.ca/topup/")
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    submit = browser.find_element_by_class_name("submit-btn-box")

    # enter these in private.py
    username.send_keys(login_user)
    password.send_keys(login_pass + '\n')

    ## GO TO TRANSACTION PAGE
    browser.get("https://mealplan.uwo.ca/topup/index.cfm/history30")
    html_source = browser.page_source

    return scrapeFile(html_source)










