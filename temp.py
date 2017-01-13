import math
from struct import pack
import os


transSymbols = dict()

charactersList = []
for i in range(33,127): 	#readable ascii
	char = chr(i)
	charactersList.append(char)
charactersList = set(charactersList) - set(['"','#','$', '%', '&'])

def isInDict(symbol, transSymbols):
	bIsInDict = false
	for idx in range(len(symbol)):
		if symbol[idx:] in transSymbols.keys():
			bIsInDict = true
	return bIsInDict

def getFirstUnusedSymbol(dict, transSymbols ):
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
	#for k in range(0,int(math.sqrt(len(text)))):	
	for k in range(0,1):	
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

def translateDown(symbol, transSymbols, value = ''):
	if symbol in transSymbols.keys():
	for idx in range(len(symbol)):  # for idx, char in enumerate(symbol):
		if symbol[idx] in transSymbols.keys():
			value += transSymbols[symbol[idx]]
		# symbol = transSymbols[symbol[idx:]]
		else:
			value += symbol[idx]

def prepareDictionaryFile(dict, filename, transSymbols):
	maxNumber = dict[max(dict, key=dict.get)]	
	contentSymbol = ''
	contentNumber = ''
	length = 0
	countNumber = 0
	for symbol, value in dict.items():
		#print(transSymbols)
		#print(symbol)
		# if symbol in transSymbols.keys():
		curSymbol = ''
		if symbol in transSymbols.keys():
			symbol = transSymbols[symbol]
			for idx in range(len(symbol)):  #for idx, char in enumerate(symbol):
				if symbol[idx] in transSymbols.keys():
					curSymbol += transSymbols[symbol[idx]]
					#symbol = transSymbols[symbol[idx:]]
				else:
					curSymbol += symbol[idx]
		else:
			curSymbol = symbol
		symbol = curSymbol
		contentSymbol += (symbol + '†')
		contentNumber += (str(value) + '†')
		with open( filename + 'Symbol.txt', 'w+') as f:
			f.write(contentSymbol)
		with open( filename + 'Number.txt', 'w+') as f:
			f.write(contentNumber)
	totalLength = os.path.getsize(filename + 'Number.txt') + os.path.getsize( filename + 'Symbol.txt')
	return(totalLength)

def maxElement(d):
	mostFrequentSymbol = max(d, key=d.get)
	mostFrequentSymbolValue = d[mostFrequentSymbol]
	for key in d:
		if d[key] == mostFrequentSymbolValue:
			if key < mostFrequentSymbol:
				mostFrequentSymbol = key
	return mostFrequentSymbol