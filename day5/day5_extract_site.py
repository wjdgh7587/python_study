import os
import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_page():
#	indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
	result = requests.get(INDEED_URL)
	soup = BeautifulSoup(result.text, "html.parser")

	pagination = soup.find("div", {"class":"pagination"})

	spans = []
	pages = []

	links = pagination.find_all('a')

#Get only page number
	for link in links[:-1]:
		pages.append(int(link.string))

	max_page = pages[-1]
	return max_page
	
def extract_job(last_page):
	for page in range(last_page):
		result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")	
		print(result.status_code)