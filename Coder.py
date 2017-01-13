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

    def printCodeDict(self):
        print (self.codeDict)

    def getCodeDict(self):
        return self.codeDict

    def code(self, text):
        output = ''
        for char in text:
            output += self[char]
        return(output)

    def codeSingle(self, text):
        output = self[text]
        return (output)

    def toFile(self, input, name):
        content = []
        it=0
        paddingLen = 32 - (len(input)%32)
        padding = '0' * paddingLen
        input = input + padding
        for i in range(int(len(input)/32)):
            block = input[it:it+32]
            # print(block)
            number = int(block,2)
            content.append(number)
            it += 32         
        with open(name, "wb") as file:
            for i in content:
                file.write(pack("<I", i))
        ret = os.path.getsize(name)
        return(ret)

##main

