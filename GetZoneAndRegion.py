import requests
from bs4 import BeautifulSoup
from accessDB import *

website = "https://ffxiv.gamerescape.com"

def getZoneandRegion(location):
	output = ["",""]
	#check if the location is in the database
	dbInfo = obtainLocation(location)
	if dbInfo:
		output = dbInfo
	else:
		#if not in database, scrape the website
		#website prefix is https://ffxiv.gamerescape.com/wiki/
		page = requests.get(website+location)
		soup = BeautifulSoup(page.text, "html.parser")
		#narrowing down search for the specific item we need
		for entry in soup.findAll("table",{"class": "rightbox"}):
			for tr in entry.findAll('tr', {"class": ""}):
				for items in tr.findAll('a'): 
					if items.has_attr("href") and str(items.attrs["href"])=="/wiki/Category:Zone": 
						output[1] = tr.contents[len(tr.contents)-1].find('a').text
					if items.has_attr("href") and str(items.attrs["href"])=="/wiki/Category:Region": 
						output[0] = tr.contents[len(tr.contents)-1].find('a').text
		#if Zone is not found, then the page is the Zone
		if output[1] == "":
			head = soup.find('h1', {"id": "firstHeading"})
			output[1]=head.text
		#add item to database
		updateLocation(location, output[0], output[1])

	return output

#same as above but, just gets the region
def getRegion(location):
	dbInfo = obtainRegion(location)
	if dbInfo:
		return dbInfo
	else:
		page = requests.get(website+location)
		soup = BeautifulSoup(page.text, "html.parser")
		for entry in soup.findAll("table",{"class": "rightbox"}):
			for tr in entry.findAll('tr', {"class": ""}):
				for items in tr.findAll('a'): 
					if items.has_attr("href") and str(items.attrs["href"])=="/wiki/Category:Region": 
						zone = str(tr.contents[len(tr.contents)-1].find('a').text)
						insertRegion(location, region)
						return region
	return None