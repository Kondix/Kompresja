import math


transSymbols = dict()

charactersList = []
for i in range(33,127): 	#readable ascii
	char = chr(i)
	charactersList.append(char)
charactersList = set(charactersList)

def getFirstUnusedSymbol(dict, transSymbols):
	unused = charactersList - set(dict.keys())   
	unused = unused - set(transSymbols.keys())
	if len(sorted(unused)) > 0:
		return(sorted(unused)[0])
	else:
		return('†')

def getPlainTextFromFile(filename):
	try:
		with open(filename) as f:
			text = f.read()
	except:
		print('Error with input file.')
	return(text)

def getNCharSet(text):
	charList = []
	for k in range(0,int(math.sqrt(len(text)))):	
		for i in range(len(text)-(k+1)):
			symbol = text[i:(i+k+2)]
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

def getNCharStatistics(text):
	characters = getNCharSet(text)
	number = []
	for char in characters:
		count = text.count(char)
		number.append(count)
	statsDict = dict(zip(characters, number))
	return(statsDict)

def prepareDictionaryFile(dict, filename, transSymbols):
	maxNumber = dict[max(dict, key=dict.get)]	#maximum number of the symbol in text
	#maxNumberHex = (hex(maxNumber)[2:])
	#if len(maxNumberHex)% 2 == 1:		#for padding
	#	maxNumberHex = '0' + maxNumberHex
	contentSymbol = ''
	contentNumber = ''
	length = 0
	countNumber = 0
	for symbol, value in dict.items():
		#number = ''
		# hexValue = hex(value)[2:]
		# for i in range(len(maxNumberHex)-len(hexValue)):	#dlugosc maksymalnego - dlugosc kodowanego, np. 0xffff - 0x3 dopisze 3 zera: 0x0003  
		# 	hexValue = '0' + hexValue
		# for i in range(int(len(maxNumberHex)/2)):
		# 	hexVal = hexValue[i] + hexValue[i+1]
		# 	char = chr(int(hexVal, 16))
		# 	number += char
		# 	i+=1
		while symbol in transSymbols.keys():
			print(symbol)
			symbol = transSymbols[symbol]
		contentSymbol += (symbol + '†')
		contentNumber += (str(value) + '†')
		with open( filename + 'Symbol.txt', 'w+') as f:
			f.write(contentSymbol)
		with open( filename + 'Number.txt', 'w+') as f:
			f.write(contentNumber)
	totalLength = length + len(dict.keys())
	return(totalLength)


	



# input = 'input.txt' ##todo argv sys
# text = getPlainTextFromFile(input)

# myMap = getTextStatistics(text) 
# #print(myMap)
# print(prepareDictionaryFile(myMap, 'old'))



# myMap = getNCharStatistics(text)
# #print(myMap)

# mostFrequentSymbol = max(myMap, key=myMap.get)
# #print(mostFrequentSymbol)

# newSymbol = getFirstUnusedSymbol(myMap)
# if newSymbol == '†':
# 	pass
# else:
# 	newText = text.replace(mostFrequentSymbol, newSymbol)

# transSymbols.update({newSymbol:mostFrequentSymbol})

# myMap = getTextStatistics(newText) 
# #print(myMap)
# print(prepareDictionaryFile(myMap, 'new'))

