# BEFORE RUNNING THIS FILE, GO INTO PRIVATE.PY AND ENTER YOUR CREDENTIALS FOR UWO LOGIN
# this file logs into the website and scrapes + creates list of transactions

from scrape import *

from selenium import webdriver
from private import *

## UWO LOGIN TO CAMPUS MEAL PLAN
browser = webdriver.Chrome("C:/Users/Sajin Kowser/Downloads/chromedriver")
browser.get("https://mealplan.uwo.ca/topup/")
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
submit = browser.find_element_by_class_name("submit-btn-box")

# enter these in private.py
username.send_keys(login_user)
password.send_keys(login_pass)
submit.click()

## GO TO TRANSACTION PAGE
browser.get("https://mealplan.uwo.ca/topup/index.cfm/history30")
html_source = browser.page_source

scrapeFile(html_source)










