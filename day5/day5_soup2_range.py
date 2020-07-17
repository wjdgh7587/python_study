#import os
#import requests
#from bs4 import BeautifulSoup
#
#indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
#
#indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
#
#pagination = indeed_soup.find("div", {"class":"pagination"})
#
#spans = []
#pages = []
#
#links = pagination.find_all('a')
#
##Get only page number
#for link in links[:-1]:
#	pages.append(int(link.string))
#
#max_page = pages[-1]
from day5_extract_site import extract_page, extract_job

max_indeed_pages = extract_page()

extract_job(max_indeed_pages)
print(max_indeed_pages)
#for n in range(max_page):
#	print(f"start={n*50}")
#	print(n)
#print(max_page)
#	print(page.find("span"))
	
	
#######################################
#      INSTALL OF BEAUTIFULSOUP4. 	  #
#######################################


# pip3 install beautifulsoup4
