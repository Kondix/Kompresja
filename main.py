from TreeBuilder import TreeBuilder
from temp import *
import os
from Coder import Coder
import collections
from Decoder import Decoder

input = ['input.txt', 'lorem_ipsum.txt', 'cholda_teaching.txt', 'cpp.txt', 'json.txt', 'pantadeusz.txt']
inputIndex = 0
maxIteration = 6

def Decode(input, msg, coder, transSymbols = None):
    print("----------")
    print("Wejscie: " + input)
    decoder = Decoder(None, None, coder)
    if transSymbols != None:
        print("Zdekodowano: " + decoder.DecodeAllLevelsString(msg, transSymbols))
    else:
        print("Zdekodowano: " + decoder.DecodeString(msg))
    print("----------")

def Initiate(singleCharDict):
    treeBuilder = TreeBuilder(singleCharDict)
    treeBuilder.Run()
    coder = Coder(treeBuilder.GetRoot()[0])
    coder.Run()
    return coder

def PrintStatistics(rozmiar):
    rozmiar = collections.OrderedDict(sorted(rozmiar.items(), key = lambda rozmiar: int(rozmiar[0])))
    for idx in rozmiar.keys():
        print("Iteracja: " + idx + " stosunek rozmiaru: " + str(rozmiar[idx]/inputsize))

text = getPlainTextFromFile(input[inputIndex])
inputsize = os.path.getsize(input[inputIndex])
optimalSize = os.path.getsize(input[inputIndex])
continueCondition = True
it = 0
rozmiar = {}

while continueCondition:
    singleCharDict = getTextStatistics(text)
    coder = Initiate(singleCharDict)
    msg = coder.code(text)

    dictSize = prepareDictionaryFile(singleCharDict, 'new', transSymbols)
    codeSize = coder.toFile(msg,'outputFile'+str(it)+'.bin')
    print("iteracja " + str(it) + ". aktualny rozmiar: " + str(dictSize) + " bytes (slownik) oraz " + str(codeSize) + " bytes (output). Poprzednio: " + str(optimalSize))

    rozmiar[str(it)] = dictSize + codeSize
    optimalSize = (dictSize + codeSize)
    bestCharDict = singleCharDict
    multiCharDict = getNCharStatistics(text, 1)
    mostFrequentSymbol = maxElement(multiCharDict)
    newSymbol = getFirstUnusedSymbol(multiCharDict, transSymbols)
    print("Najczestszy symbol: " + mostFrequentSymbol)
    print("Podmieniono na: " + newSymbol)

    if newSymbol == '†':
        break
    bestText = text
    text = text.replace(mostFrequentSymbol, newSymbol)
    transSymbols[newSymbol] = mostFrequentSymbol

    it += 1
    if it==maxIteration:
        break


coder = Initiate(bestCharDict)
msg = coder.code(bestText)

print("Najblepszy słownik: " + str(transSymbols))
Decode(bestText, msg, coder, transSymbols)

dictSize = prepareDictionaryFile(bestCharDict, 'new', transSymbols)
codeSize = coder.toFile(msg,'ostatecznyOutput.bin')

PrintStatistics(rozmiar)