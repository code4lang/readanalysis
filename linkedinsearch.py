
import requests
from bs4 import BeautifulSoup

# Replace these values with your own
search_query = "Tesla data engineer"
base_url = "https://www.linkedin.com/search/"

# Make a request to the search page and parse HTML content using BeautifulSoup
response = requests.get(f'{base_url}?keywords={search_query}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'})
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# Find all the search results that match our query and extract names
results = soup.find_all('li', {'class': 'search-result'})
names = []
for result in results:
    name = result.find('a', {'class': 'result__title'}).text.strip()
    names.append(name)
print(names)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these values with your own
username = "your_email@linkedin.com"
password = "your_password"
search_query = "Tesla data engineer"
base_url = "https://www.linkedin.com/search/"

# Set up the webdriver and navigate to LinkedIn login page
options = webdriver.ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(executable_path="chromedriver", options=options)
browser.get("https://www.linkedin.com/login")

# Locate the email and password input fields and submit the login form using Selenium
email = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "session_key")))
password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "session_password")))
email.send_keys(username)
password.send_keys(password + Keys.RETURN)
time.sleep(5) # wait for page to load after login

# Navigate to search results page and scrape names of data engineers working at Tesla
browser.get(f'{base_url}?keywords={search_query}')
time.sleep(5) # wait for page to load
results = browser.find_elements_by_xpath("//li[@class='search-result']")
names = []
for result in results:
    name = result.find_element_by_xpath(".//a[@class='result__title']").text.strip()
    names.append(name)
print(names)
'''Replace `username`, `password`, `search_query`, etc., with your own values, and modify the script as 
needed to suit your specific requirements. This script uses Selenium WebDriver to automate the login process 
and scrape search results from LinkedIn after logging in. Note that using a headless browser 
(`options.add_argument("--headless")`) can be beneficial to avoid being detected as an automated tool, but you
 may need to remove it or modify the code if you want a more interactive experience or support for visual elements.'''


import os
from requests_oauthlib import OAuth2Session

# Replace these values with your own
client_id = "xxxxxxxxxxxxxxxxxxxxxxxxx"
redirect_uri = "http://localhost:8000/callback"
client_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Create OAuth2Session object and initialize authorization
authorization_url = "https://www.linkedin.com/oauth/v2/authorization"
token_url = "https://www.linkedin.com/oauth/v2/accessToken"
token_type_url = "https://www.linkedin.com/oauth/v2/tokenInfo"

auth = OAuth2Session(client_id=client_id)
authorization_response = input("Go to the following link in your browser then type the "+
                               "authorization code here: ")
access_token = auth.fetch_token(token_url, authorization_response, client_secret=client_secret)
refresh_token = access_token['refreshToken']
r = auth.refresh_token(token_type_url, refresh_token)
access_token = r['accessToken']
auth.set_access_token(access_token)



import json
from linkedin import client, pagination

# Replace these values with your own
company = "Tesla"
search_query = f'({company}) data engineer'

# Authenticate using the authorized session object created earlier
api = client.LinkedInRestClient(
    version='201902', accessToken=auth.access_token, clientSecret=client_secret)
search_results = pagination.SearchPaginator(api, query=search_query, resultsPerPage=50, sortOrder="DESC")
for page in search_results:
    for member in page.elements:
        print(member.firstName + " " + member.lastName)

'''
Replace the placeholders with your own company name and job title, and replace `client_id`, `client_secret`,
`redirect_uri`, etc., from the first block of code. This example assumes you have already registered an app 
on LinkedIn Developer and obtained a client ID, secret key, etc.

This script searches for data engineers working at Tesla using the LinkedIn Search API, which requires OAuth
 authentication. You can modify the search query to suit your specific requirements, and this code can be
   extended further to extract more detailed information from each result returned by the API. Note that 
   LinkedIn's terms of service prohibit scraping or automating their site without explicit consent, so be
     sure to follow their policies and guidelines.'''