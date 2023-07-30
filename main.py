from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_binary_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options.binary_location = chrome_binary_path

browser = webdriver.Chrome(service=Service(), options=chrome_options)

base_url = 'https://kr.indeed.com/jobs?q='
search_term = 'python'

browser.get('https://kr.indeed.com/jobs?q=python&limit=50')

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_='jobsearch-ResultsList')
jobs = job_list.find_all('li', recursive=False)
for job in jobs:
    print(job)
    print("/////")