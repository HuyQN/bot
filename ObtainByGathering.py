from bs4 import BeautifulSoup
from GetZoneAndRegion import getRegion

def obtainByGathering(table):
	#print(table)
	results = []
	#check each element in the table for a gathering location
	for boxes in table.findAll('tr'):
		if not boxes.find('a'):
			continue
		#The contents of elements is 
		#['\n', The Location,'\n', node information, '\n', gathering requirements]
		elements = boxes.contents
		# the first small for now is always the location
		small = elements[1].find('small')
		location = getRegion(small.contents[3].attrs['href'])
		#the gathering job
		gJob = ""
		if "Mining" in small.contents[0].text:
			gJob = "Mining"
		elif "Harvesting" in small.contents[0].text:
			gJob = "Harvesting"
		#Information about the node: level, type, and time if applicable
		nodeInfo = elements[3].find('small').contents
		results.append([location, str(small.contents[3].text + small.contents[4]), gJob, nodeInfo[0]+" "+nodeInfo[2]]) 
	return results
