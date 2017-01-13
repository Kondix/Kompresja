from TreeBuilder import TreeBuilder, HoffmanNode
from temp import *
import binascii
import time
from struct import pack
import os
from Coder import Coder
import collections

# input = 'input.txt'
# input = 'lorem_ipsum.txt'
#
# input = 'cholda_teaching.txt'
#
# input = 'cpp.txt'
#
input = 'json.txt'
# input = 'Tibia.exe'
# input = 'pantadeusz.txt'

text = getPlainTextFromFile(input)
inputsize = os.path.getsize(input);
optimalSize = os.path.getsize(input) #999999999999999999999999999
continueCondition = True
it = 0

rozmiar = {}
while continueCondition:
    singleCharDict = getTextStatistics(text)
    treeBuilder = TreeBuilder(singleCharDict)
    # print(singleCharDict)
    treeBuilder.Run()
    coder = Coder(treeBuilder.GetRoot()[0])
    coder.Run()
    coder.printCodeDict()
    msg = coder.code(text)
    # print(coder.codeDict)
    dictSize = prepareDictionaryFile(singleCharDict, 'new', transSymbols)
    codeSize = coder.toFile(msg,'outputFile'+str(it)+'.bin')
    print("iteracja " + str(it) + ". aktualny rozmiar: " + str(dictSize) + " bytes (slownik) oraz " + str(codeSize) + " bytes (output). Poprzednio: " + str(optimalSize))
    rozmiar[str(it)] = dictSize + codeSize
    # if optimalSize < (dictSize + codeSize):
    #     #break
    optimalSize = (dictSize + codeSize)
    bestCharDict = singleCharDict
    multiCharDict = getNCharStatistics(text)
    mostFrequentSymbol = maxElement(multiCharDict) #max(multiCharDict, key=multiCharDict.get)
    newSymbol = getFirstUnusedSymbol(multiCharDict, transSymbols)
    if newSymbol == '†':
        break
    bestText = text
    text = text.replace(mostFrequentSymbol, newSymbol)
    transSymbols.update({newSymbol:mostFrequentSymbol})
    it += 1
    if it==100:
        break



treeBuilder = TreeBuilder(bestCharDict)
treeBuilder.Run()
coder = Coder(treeBuilder.GetRoot()[0])
coder.Run()
msg = coder.code(bestText)
dictSize = prepareDictionaryFile(bestCharDict, 'new', transSymbols)
codeSize = coder.toFile(msg,'ostatecznyOutput.bin')
# coder.printCodeDict()


rozmiar = collections.OrderedDict(sorted(rozmiar.items(), key = lambda rozmiar: int(rozmiar[0])))

for idx in rozmiar.keys():
    print("Iteracja: " + idx + " stosunek rozmiaru: " + str(rozmiar[idx]/inputsize))