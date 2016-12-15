charactersList = []
for i in range(1,255): 	#readable ascii
	char = chr(i)
	charactersList.append(char)

def getPlainTextFromFile(filename):
	try:
		with open(filename) as f:
			text = f.read()
	except:
		print('Error with input file.')
	return(text)

def getDoubleCharSet(text):
	charList = []
	for i in range(len(text)-1):
		symbol = text[i] + text[i+1]
		charList.append(symbol)
	charList = sorted(set(charList))
	return(charList)

def getTextStatistics(text):
	characters = sorted(set(text)) #<- set() aaabbb - ab
	number = []
	for char in characters:
		count = text.count(char)
		number.append(count)
	statsDict = dict(zip(characters, number))
	return(statsDict)

def getDoubleCharStatistics(text):
	characters = getDoubleCharSet(text)
	number = []
	for char in characters:
		count = text.count(char)
		number.append(count)
	statsDict = dict(zip(characters, number))
	return(statsDict)

# def prepareDictionaryFile(dict):
# 	maxNumber = dict[max(dict, key=dict.get)]	#maximum number of the symbol in text
# 	maxNumberHex = (hex(maxNumber)[2:])
# 	if len(maxNumberHex)% 2 == 1:		#for padding
# 		maxNumberHex = '0' + maxNumberHex
# 	#content = []
# 	for symbol, value in dict.items():
# 		number = ''
# 		hexValue = hex(value)[2:]
# 		for i in range(len(maxNumberHex)-len(hexValue)):	#dlugosc maksymalnego - dlugosc kodowanego, np. 0xffff - 0x3 dopisze 3 zera: 0x0003  
# 			hexValue = '0' + hexValue
# 		for i in range(int(len(maxNumberHex)/2)):
# 			hexVal = hexValue[i] + hexValue[i+1]
# 			char = chr(int(hexVal, 16))
# 			number += char
# 			i+=1
# 		#content.append([number, symbol])
# 		#for item in content:
# 		with open(('dict\\' + item[1], 'w+')) as f:
# 			f.write(item)
# 	return(content)

def prepareDictionaryFile(dict, dirName):
	maxNumber = dict[max(dict, key=dict.get)]	#maximum number of the symbol in text
	size = 0
	for symbol, value in dict.items():
		#size += len(symbol)
		hexValue = hex(value)[2:]
		number = ''
		if len(hexValue)% 2 == 1:		#for padding
			hexValue = '0' + hexValue
		for i in range(int(len(hexValue)/2)):
			hexVal = hexValue[i] + hexValue[i+1]
			char = chr(int(hexVal, 16))
			i+=1
			number += char
		with open((dirName + '\\' + symbol), 'a+') as f:
			f.write(number)
			size += len(number)
	return(size)


	



# input = 'input.txt' ##todo argv sys
# text = getPlainTextFromFile(input)

# myMap = getTextStatistics(text) 
# #print(myMap)

# myMap = getDoubleCharStatistics(text)
# #print(myMap)

# topDoubleChar = max(myMap, key=myMap.get)
# #print(topDoubleChar)

# newText = text.replace(topDoubleChar, 'x')
# #print(newText)

# print(prepareDictionaryFile(myMap,'olddict'))
