from TreeBuilder import TreeBuilder, HoffmanNode
from temp import *
import binascii
import time
from struct import pack
import os

class Coder():
    def __init__(self, treeRoot):
        self.treeRoot = treeRoot
        self.codeDict = {}

    def __getitem__(self, symbol):
        return self.codeDict[str(symbol)]

    def Run(self):
        self.CodeSingleNode(self.treeRoot, '')

    def CodeSingleNode(self, node, code):
        if (node.GetLeft() != None):
            leftCode = code + '0'
            self.CodeSingleNode(node.GetLeft(), leftCode)
        if (node.GetRight() != None):
            rightCode = code + '1'
            self.CodeSingleNode(node.GetRight(), rightCode)
        if (node.GetSymbol() != None):
            self.codeDict[node.GetSymbol()] = code

    def code(self, text):
        output = ''
        for char in text:
            output += self[char]
        return(output)

    def toFile(self, input, name):
        content = []
        it=0
        paddingLen = 32 - (len(input)%32)
        padding = '0' * paddingLen
        input = input + padding
        for i in range(int(len(input)/32)):
            block = input[it:it+32]
            number = int(block,2)
            content.append(number)
            it += 32         
        with open(name, "wb") as file:
            for i in content:
                file.write(pack("<I", i))
        ret = os.path.getsize(name)
        return(ret)

##main


input = 'input.txt'

text = getPlainTextFromFile(input)
optimalSize = os.path.getsize(input) #999999999999999999999999999
continueCondition = True
it = 0

while continueCondition:
    singleCharDict = getTextStatistics(text)
    treeBuilder = TreeBuilder(singleCharDict)
    treeBuilder.Run()
    coder = Coder(treeBuilder.GetRoot()[0])
    coder.Run()
    msg = coder.code(text)
    dictSize = prepareDictionaryFile(singleCharDict, 'new', transSymbols)
    codeSize = coder.toFile(msg,'outputFile'+str(it)+'.bin')
    if optimalSize <= (dictSize + codeSize):
        break
    optimalSize = (dictSize + codeSize)
    bestCharDict = singleCharDict
    multiCharDict = getNCharStatistics(text)
    mostFrequentSymbol = maxElement(multiCharDict) #max(multiCharDict, key=multiCharDict.get)
    newSymbol = getFirstUnusedSymbol(multiCharDict, transSymbols)
    if newSymbol == '†':
        break
    text = text.replace(mostFrequentSymbol, newSymbol)
    transSymbols.update({newSymbol:mostFrequentSymbol})
    it += 1
    if it==3:
        break



treeBuilder = TreeBuilder(bestCharDict)
treeBuilder.Run()
coder = Coder(treeBuilder.GetRoot()[0])
coder.Run()
msg = coder.code(text)
dictSize = prepareDictionaryFile(bestCharDict, 'new', transSymbols)
codeSize = coder.toFile(msg,'outputFile')
