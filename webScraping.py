from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Users/stefa/chrome/chromedriver")

driver.get("http://www.fip.it/risultati.aspx?com=RTN&IDRegione=TN&IDProvincia=TN")

print(driver)