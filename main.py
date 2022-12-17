from selenium import webdriver
from config.options import options


browser = webdriver.Chrome(options=options)

# Selenium 사용하는 예시
browser.get("https://google.com")
browser.save_screenshot("success.png")
