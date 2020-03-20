from bs4 import BeautifulSoup

def acquiredFromDuty(table):
	result = []
	#find the instance for each element in the table
	for elements in table.findAll('td'):
		result.append(elements.text.lstrip().rstrip("\n"))
	return result