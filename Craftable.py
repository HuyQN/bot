from bs4 import BeautifulSoup

def craftable(entry):
	test = entry.find('tbody').find('tr')
	#testing if the table is a crafting recipe
	possibleCraft = test.findAll('a')
	#A recipe needs to have an href, and in it needs to have Category and Recipe
	for x in possibleCraft:
		if x.has_attr('href'):
			if (("Category:" in x.attrs['href']) and ("Recipe" in x.attrs['href'])):
				#checking if there is a level associated with the element we need
				if len((test.contents[1].contents)) == 2:
					#Obtain the crafting class
					cClass = str(test.contents[1].contents[0].text)
					#obtain the level requirement
					#array is needed for char, range will not work
					level = str(test.contents[1].contents[1])
					recipeLevel = ''.join(filter(lambda x: x in ['1','2','3','4','5','6','7','8','9','0'], level))
					return f"Level {recipeLevel} {cClass} Recipe"

	return ""

	#broken test algorithm
	'''if test.find('td') and len(test.contents) == 2:
		print(str(test.contents)+'\n')
		test2 = test.find('td').find('div')
		if test2:
			#print(str(test.contents[1].contents)+'\n')
			print(test2)
			cClass = str(test.contents[1].contents[0].attrs['title'])
			recipeLevel = str(test.contents[1].contents[1][1:])
			return str(f"Level{recipeLevel} {cClass} Recipe")'''
	return ""