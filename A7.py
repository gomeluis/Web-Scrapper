###########################################
#   Luis Gomez                            #
#   CPSC 340 - Assignment 7: Web Scraping #
#   12/1/2017                             #
###########################################

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
websites = []
count = 0 

##### For Testing purposes
## def displayArray(): 
##    for i in range(0,len(websites)):
##        print(str(i) + ": " + websites[i])
######

def searchWebsites():  
    for link in bsObj.findAll('span',{'class':'flagicon'} ):
        hrefLink = link.find_next('a', href=True)
        linkToStates = "https://en.wikipedia.org" + hrefLink.get('href')
        websites.append(linkToStates)
       
        
        

def findStateInfo(websites):
    global count 
    for a in websites:
        html = urlopen(a)
        bsObj = BeautifulSoup(html.read(),"html.parser")
        count += 1
        for x in bsObj.findAll('table', {'class':'infobox geography vcard'}):
            try:
                
                 name = x.find("th", {'class': "fn org"}).get_text()
                 
                 findCapTag = x.find("tr", {'class': 'mergedtoprow'})
                 capital = findCapTag.find("td").get_text()
                 
                 #couldnt get the population
                 #findPopTag = x.find("th", text="• Total").                             
                 #print(findPopTag)
                 #print(findPopTag.find_previous_sibling('td').get_text())
                 
                 

                
                 
                 findWebTag = x.find("a", {'class': "external text"}).get_text()
                 findWebTag = "http://" + findWebTag + "/"
                 
                 print(count, name," ", capital, " ", "POP", " ", findWebTag)
                         
            except AttributeError:
                pass
   
searchWebsites()
findStateInfo(websites)

   
                          
    
   
                        
