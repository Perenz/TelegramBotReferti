from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#Selenium setups
driver = webdriver.Chrome("C:/Users/stefa/chrome/chromedriver")

driver.get("http://www.fip.it/risultati.aspx?com=RTN&IDRegione=TN&IDProvincia=TN")

content = driver.page_source
soup = BeautifulSoup(content, features='html5lib')

#Look for td  with luogo-arbitri class in the 'result' table inside the web page
for tag in soup.find('table', attrs={'class':'table'}).findAll('td', attrs={'class':'luogo-arbitri'}):
    # print(tag.text)

    # Filter the found tags to keep games played at 'CentroSportivoTrentoNord'
    stringa = ''.join(tag.text.split())
    if(stringa.find('CentroSportivo') != -1):
        print(stringa)
        datetime = tag.find('strong').text.split(' - ')
        print('Game date: ' + datetime[0] + '\nGame time: ' + datetime[1] + '\n\n')


    #Class 'risultati-giorno' to navigate through Championship days
    # https://www.pluralsight.com/guides/guide-scraping-dynamic-web-pages-python-selenium

    '''
    if(tag.text.translate(str.maketrans('', '', '\n\t ')).split(' - ') == "CentroSportivoTrentoNord+"):
        print(tag)
        datetime = tag.find('strong').text
        #print(datetime.split(' - '))

    '''