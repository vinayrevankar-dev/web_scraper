from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/mnt/c/DRIVERS/WebDriver/bin/chromedriver")

driver.get("https://www.nike.com/t/therma-mens-basketball-pants-2Xm3KD/CK6613-063")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

print(soup.title)
price_result = soup.find(class_= "product-price is--current-price css-1emn094")

print(price_result.get_text())

driver.close()