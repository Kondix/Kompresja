from TreeBuilder import TreeBuilder, HoffmanNode
from temp import *
import binascii

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

    def toFile(self, input, filename):
        content = ''
        if (len(input)<=8):
            return(1)
        it=0
        for i in range(int(len(input)/8)):
            block = input[it:it+8]
            number = int(block,2)
            content += (str(number) + ' ')
            it += 8
        block = input[it:]
        if block != '':
            number = int(block,2)
        content += (str(number) + ' ')
        with open(filename, 'w+') as f:
            f.write(content)
        return(int(len(input)/8)+1)





input = 'input.txt' ##todo argv sys
text = getPlainTextFromFile(input)
optimalSize = 999999999999999999999999999
continueCondition = True
it=0

while continueCondition:
    singleCharDict = getTextStatistics(text)
    treeBuilder = TreeBuilder(singleCharDict)
    treeBuilder.Run()
    coder = Coder(treeBuilder.GetRoot()[0])
    coder.Run()
    msg = coder.code(text)
    dictSize = prepareDictionaryFile(singleCharDict, 'new', transSymbols)
    codeSize = coder.toFile(msg,'outputFile')
    if optimalSize <= (dictSize + codeSize):
        break
    print(singleCharDict)
    optimalSize = (dictSize + codeSize)
    bestCharDict = singleCharDict
    multiCharDict = getNCharStatistics(text)
    mostFrequentSymbol = max(multiCharDict, key=multiCharDict.get)
    newSymbol = getFirstUnusedSymbol(multiCharDict, transSymbols)
    if newSymbol == '†':
        break
    text = text.replace(mostFrequentSymbol, newSymbol)
    transSymbols.update({newSymbol:mostFrequentSymbol})
    it += 1
    if it==100:
        break
print(it)

print(transSymbols)

treeBuilder = TreeBuilder(bestCharDict)
treeBuilder.Run()
coder = Coder(treeBuilder.GetRoot()[0])
coder.Run()
msg = coder.code(text)
dictSize = prepareDictionaryFile(bestCharDict, 'new', transSymbols)
codeSize = coder.toFile(msg,'outputFile')
