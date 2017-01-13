from TreeBuilder import TreeBuilder, HoffmanNode
from temp import *
import binascii
import time
from struct import pack
import os
from Coder import Coder


input = 'input.txt'

text = getPlainTextFromFile(input)
optimalSize = os.path.getsize(input) #999999999999999999999999999
continueCondition = True
it = 0


while continueCondition:
    singleCharDict = getTextStatistics(text)
    treeBuilder = TreeBuilder(singleCharDict)
    print(singleCharDict)
    treeBuilder.Run()
    coder = Coder(treeBuilder.GetRoot()[0])
    coder.Run()
    coder.printCodeDict()
    msg = coder.code(text)
    #print(coder.codeDict)
    dictSize = prepareDictionaryFile(singleCharDict, 'new', transSymbols)
    codeSize = coder.toFile(msg,'outputFile'+str(it)+'.bin')
    #print("iteracja " + str(it) + ". aktualny rozmiar: " + str(dictSize) + " bytes (slownik) oraz " + str(codeSize) + " bytes (output). Lacznie: " + str(optimalSize))
    if optimalSize < (dictSize + codeSize): 
        print("opanie")
        #break
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
    if it==3:
        break



# treeBuilder = TreeBuilder(bestCharDict)
# treeBuilder.Run()
# coder = Coder(treeBuilder.GetRoot()[0])
# coder.Run()
# msg = coder.code(bestText)
# dictSize = prepareDictionaryFile(bestCharDict, 'new', transSymbols)
# codeSize = coder.toFile(msg,'ostatecznyOutput.bin')
