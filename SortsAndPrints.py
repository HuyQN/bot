#all of these were for better organization of information obtained, and easier reading of main module
def merchantSort(arr):
	output = ""
	arr.sort()
	for elements in arr:
		#output += felements[1] + " by " + elements[2] + "\n"
		output += f"{elements[1]} by {elements[2]}\n"
	return output

def gatherSort(arr):
	output = ""
	arr.sort()
	for elements in arr:
		#output += elements[1] + " " + elements[3] + " by " + elements[2]
		output += f"{elements[1]} {elements[3]} by {elements[2]}\n"
	return output

def arrPrint(arr):
	output =""
	for elements in arr:
		#output += elements + "\n"
		output += f"{elements}\n"
	return output

def arrSort(arr):
	output =""
	arr.sort()
	for elements in arr:
		#output += elements+"\n"
		output += f"{elements}+\n"
	return output