import os
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

spans = []
pages = []

#pages = pagination.find_all('a')
links = pagination.find_all('a')


#for page in pages:
#	spans.append(page.find("span"))

#Get only page number
for link in links[:-1]:
#	pages.append(link.find("span").string)
	pages.append(int(link.string))

#print(spans[:-1])
#print(spans[0:5])
#print(spans[0:-1])
#pages = pages[0:-1]
max_page = pages[-1]
print(max_page)
#	print(page.find("span"))
	
	
#######################################
#      INSTALL OF BEAUTIFULSOUP4. 	  #
#######################################


# pip3 install beautifulsoup4
