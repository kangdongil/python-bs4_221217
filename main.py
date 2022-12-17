from selenium import webdriver
from config.options import options
from bs4 import BeautifulSoup


base_url = "https://kr.indeed.com/jobs?q="
keyword = "python"

browser = webdriver.Chrome(options=options)
browser.get(f"{base_url}{keyword}")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone is not None:
        continue
