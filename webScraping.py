from selenium import webdriver

from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import pandas as pd

#Selenium setups
driver = webdriver.Chrome("C:/Users/stefa/chrome/chromedriver")
driver.implicitly_wait(10)
driver.get("http://www.fip.it/risultati.aspx?com=RTN&IDRegione=TN&IDProvincia=TN")

content = driver.page_source
soup = BeautifulSoup(content, features='html5lib')

#id: content-menu-campionati

#Fetch all the href link to league days
#class: risultati-giorno
# links = soup.find_element_by_xpath("//*div[@class='risultati-giorno']")


'''
LINK DIRETTO AI RISULTATI:
      http://www.fip.it/risultati.aspx?com=RTN&sesso=M&camp=D&fase=1&girone=39727&ar=0&turno=5&IDRegione=&IDProvincia=




link = driver.find_elements_by_class_name('risultati-giorno')
link = link[:len(link)//2]
#link = soup.select("div.risultati-giorno a[href]")
print(len(link))
ctr = 0
for l in link:
    ctr += 1
    print(str(ctr) + ': ' + str(l))
    #Il problema potrebbe essere che il click sull'elemento viene fatto prima che questo sia completamente caricato
    #Soluz: prendere il link e navigare tramite link invece che tramite elemento
    
    
      variazioni: ar=0/1
      turno = 1..11 in SerieD (DIPENDE DAL CAMPIONATO)
    try:
        l.click()
    except:
        print("Exception DEBUG")
        pass

'''

resHref = "http://www.fip.it/risultati.aspx?com=RTN&sesso=M&camp=D&fase=1&girone=39727&ar={}&turno={}&IDRegione=&IDProvincia="

print(resHref.format(0,2))


#Take the number of games
links = soup.findAll('div', attrs={'class':'risultati-giorno'})
linksNum = len(links[:len(links)//4]) # /2 Because of mobile/web view and /2 because of AR

for i in [1,0]: #AR
    for j in range(1, linksNum+1):
        #print(resHref.format(i,j))
        driver.get(resHref.format(i,j))

        '''
        Do stuff into the page:
            -Take all the game
            -Choose those with Gardolo basket playing @ home
        '''
        #Look for td  with luogo-arbitri class in the 'result' table inside the web page
        #link = driver.find_elements_by_class_name('risultati-giorno')
        #for tag in soup.find('table', attrs={'class':'table'}).findAll('td', attrs={'class':'luogo-arbitri'}):
        for tag in driver.find_elements_by_class_name('luogo-arbitri'):
            # print(tag.text)

            # Filter the found tags to keep games played at 'CentroSportivoTrentoNord'
            stringa = tag.text

            #Remove empty strings
            if stringa != '':
                stringhe = stringa.split('\n') #Stringhe[0] with place, strihgne[1] with datetime
                
                place = stringhe[0]
                if(place.find('Centro Sportivo') != -1):
                    print(place)
                    datetime = stringhe[1].split(' - ')
                    print('Game date: ' + datetime[0] + '\nGame time: ' + datetime[1] + '\n\n')
        
    #Class 'risultati-giorno' to navigate through Championship days
    # https://www.pluralsight.com/guides/guide-scraping-dynamic-web-pages-python-selenium
    # https://www.seleniumhq.org/docs/

'''
for tag in driver.find_elements_by_class_name('luogo-arbitri'):
            # print(tag.text)

            # Filter the found tags to keep games played at 'CentroSportivoTrentoNord'
            stringa = tag.text

            #Remove empty strings
            if stringa != '':
                stringhe = stringa.split('\n') #Stringhe[0] with place, strihgne[1] with datetime
                
                place = stringhe[0]
                if(place.find('Centro Sportivo Trento Nord') != -1):
                    print(place)
                    datetime = stringhe[1].split(' - ')
                    print('Game date: ' + datetime[0] + '\nGame time: ' + datetime[1] + '\n\n')
'''

'''
TEMPORARY NOT NECESSARY

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
