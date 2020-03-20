import requests
from bs4 import BeautifulSoup

from SortsAndPrints import *

from SoldByMerchant import soldByMerchant
from AcquiredFromDuty import acquiredFromDuty
from ObtainByGathering import obtainByGathering
from Craftable import craftable
from accessDB import *

from urllib.parse import quote

website = "https://ffxiv.gamerescape.com"
wiki = "/wiki"

#Obtain the page for the item, and use other methods to scrape for 
#information needed
def item_scraping(item):
	#changes the item to website extention
	capItem = quote(item)
	#URL = website+wiki+"/"+capItem
	URL = f"{website}{wiki}/{capItem}"
	page = requests.get(URL)
	#soup is the html code
	soup = BeautifulSoup(page.text, "html.parser")
	#if page is not found	
	if(page.status_code == 404):
		#searches for item
		URL = f"{website}/w/index.php?search={capItem}"
		page = requests.get(URL)
		soup = BeautifulSoup(page.text, "html.parser")
		fhead = soup.find('h1',{'id': 'firstHeading'})
		#if the items doesn't redirect, then the following will be true
		if fhead and (fhead.text == "Search results"):
			#old brute force method used
			'''capItemPlus = capItem.replace("_","+")
			URL = f"{website}/w/index.php?search={capItemPlus}"
			page = requests.get(URL)
			soup = BeautifulSoup(page.text, "html.parser")'''
			#future usage for getting possible other items that can be searched
			for boxes in soup.findAll('h2'):
				heading = boxes.find('span')
				if heading and heading.text == "Page title matches":
					return "Item cannot be found"
			return "Item cannot be found"
	#if connection is timed out
	if(page.status_code == 408 or page.status_code == 503):
		output = obtainSearchItem(capItem)
		if output:
			return output
		else:
			return f"{website} currently unavailable"
	else:
		#f = open("text.txt","w+", encoding = 'utf-8')
		output = URL+"\n"
		#searches for every table for a table without a table inside of it
		for entry in soup.findAll("table"):
			if(not entry.find("table")):
				#checks if the table is a Recipe
				output += craftable(entry)
				#then checks the header of the table, and uses the appropriate function
				for info in entry.findAll('th'):
					if("Merchant" in info.text):
						merchants = soldByMerchant(entry)
						if merchants != []:
							output += "Can be bought by merchants\n"
							output += merchantSort(merchants) + "\n"

					if("Duty" in info.text):
						output += "Can acquire from duty\n"
						output += arrPrint(acquiredFromDuty(entry)) + "\n"

					if("Node (Slot)" in info.text):
						output += "Can obtain by gathering\n"
						output += gatherSort(obtainByGathering(entry)) + "\n"
		#inputs the command to the database
		updateSearchItem(capItem, output)
		return output

	#old bruteforce method to obtain the address of the item
	#Change the string to be able to obtain the item's page
'''def itemParsing(word):
	#Capitalize the first letter of every word
	word = word.lower()
	word = word.capitalize()
	word = word.rstrip(' -')
	for char_num in range(len(word)):
		if word[char_num] is ' ' or word[char_num] is '-':
			 word = word[:char_num+1] + word[char_num+1].swapcase() + word[(char_num+2):]
	#replace every space with '_' so it can be attached to the website
	#to obtain the item's page
	return word.replace(" ","_")
'''

print(item_scraping("hipotion"))
#print(item_scraping("darksteel ore"))
#print(item_scraping("bronze ingot"))
#print(item_scraping("stonefly larva"))
