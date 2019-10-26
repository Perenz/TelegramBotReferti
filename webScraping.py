from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

#Selenium setups
driver = webdriver.Chrome("C:/Users/stefa/chrome/chromedriver")

driver.get("http://www.fip.it/risultati.aspx?com=RTN&IDRegione=TN&IDProvincia=TN")

content = driver.page_source
soup = BeautifulSoup(content, features='html5lib')

#id: content-menu-campionati

#Fetch all the href link to league days
#class: risultati-giorno
# links = soup.find_element_by_xpath("//*div[@class='risultati-giorno']")


link = driver.find_elements_by_class_name('risultati-giorno')
link = link[:len(link)//2]
#link = soup.select("div.risultati-giorno a[href]")
print(len(link))
ctr = 0
for l in link:
    ctr += 1
    print(str(ctr) + ': ' + str(l))
    #Il problema potrebbe essere che il click sull'elemento viene fatto prima che questo sia completamente caricato
    l.click()

'''
links = soup.findAll('div', attrs={'class':'risultati-giorno'})
links = links[:len(links)//2]
ctrLi = 0
ctrL = 0
print(len(links))
for l in links:
    for li in l:
        ctrLi += 1
        #li.get('href').click()
        #print(str(ctrLi) +': ' + li.get('href'))
        #res = driver.execute_script("javascript:getRisultatiPartite('RTN', 'M', 'D', '1', '39727', '0', '11', 'TN', 'TN')")
        #print(res)
'''

'''
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
    # https://www.seleniumhq.org/docs/
'''