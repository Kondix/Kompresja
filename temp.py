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

def getNCharSet(text, cnt):
	charList = []
	for k in range(0,cnt):
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

def getNCharStatistics(text, cnt):
	characters = getNCharSet(text, cnt)
	number = []
	for char in characters:
		count = text.count(char)
		number.append(count)
	statsDict = dict(zip(characters, number))
	return(statsDict)

def translateDown(symbol, transSymbols, value = ''):
	for idx in range(len(symbol)):  # for idx, char in enumerate(symbol):
		if symbol[idx] in transSymbols.keys():
			newSymbol = transSymbols[symbol[idx]]
			value += transSymbols[symbol[idx]]
			translateDown(newSymbol,transSymbols,value)
		# symbol = transSymbols[symbol[idx:]]
		else:
			value += symbol[idx]
	print(value)
	return(value)

def prepareDictionaryFileBackup(dict, filename, transSymbols):
	contentSymbol = ''
	contentNumber = ''
	curSymbol = ''
	for symbol, value in dict.items():
		if symbol in transSymbols.keys():
			symbol = transSymbols[symbol]
			for idx in range(len(symbol)):
				if symbol[idx] in transSymbols.keys():
					curSymbol += transSymbols[symbol[idx]]
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

def prepareDictionaryFile(dict, filename, transSymbols):
	contentSymbol = ''
	contentNumber = ''
	curSymbol = ''
	for symbol, value in dict.items():

		curSymbol = TranslateSymbol(symbol, transSymbols, curSymbol)
		print(curSymbol)
		symbol = curSymbol
		contentSymbol += (symbol + '†')
		contentNumber += (str(value) + '†')
		with open( filename + 'Symbol.txt', 'w+') as f:
			f.write(contentSymbol)
		with open( filename + 'Number.txt', 'w+') as f:
			f.write(contentNumber)
	totalLength = os.path.getsize(filename + 'Number.txt') + os.path.getsize( filename + 'Symbol.txt')
	return(totalLength)

def TranslateSymbol(input, transSymbols, translated):
	for element in input:
		if element in transSymbols.keys():
			translated = TranslateSymbol(transSymbols[element], transSymbols, translated)
		else:
			translated += element
	return translated

def maxElement(d):
	mostFrequentSymbol = max(d, key=d.get)
	mostFrequentSymbolValue = d[mostFrequentSymbol]
	for key in d:
		if d[key] == mostFrequentSymbolValue:
			if key < mostFrequentSymbol:
				mostFrequentSymbol = key
	return mostFrequentSymbol