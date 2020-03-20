from bs4 import BeautifulSoup
from GetZoneAndRegion import getZoneandRegion

#areas where we don't want to check if purchasable 
housing = ["Lavender_Beds","Mist","The_Goblet", "Shirogane"]

def soldByMerchant(table):
	#search each element in the table
	element = table.findAll('tr',{'class': ""})
	results = []
	for objects in element:
		#search for specific info
		for item in objects.findAll('td'):
			if not item.find('div'):
				#obtain merchant's name
				#merchant = item.find('a').attrs['title']
				merchant = item.find('a').text
				#first small text is the location
				smallText = item.find('small')
				loc = str(smallText.find('a').attrs["href"])
				#if not desired location, skip
				if housingLoc(loc):
					continue
				#gets location region, and zone for better info
				location = getZoneandRegion(loc)
				results.append([location[0], str(location[1]+smallText.contents[1]), merchant])
	return results

def housingLoc(href):
	#remove /wiki/ from the href
	loc = href[6:]
	if "Apartment" in loc:
		return True
	#check if from undesirable locations
	for element in housing:
		if element == loc:
			return True

