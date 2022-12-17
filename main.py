from selenium import webdriver
from config.options import options


base_url = "https://kr.indeed.com/jobs?q="
keyword = "python"

browser = webdriver.Chrome(options=options)
browser.get(f"{base_url}{keyword}")

print(browser.page_source)
browser.save_screenshot("success.png")
