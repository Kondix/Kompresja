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
        for i in range(int(len(input)/8)):
            block = input[i:i+8]
            i += 7
            number = int(block,2)
            content += chr(number)
        #content = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('binary')
        with open(filename, 'w+') as f:
            f.write(content)
        return(None)


def main():
    input = 'input.txt' ##todo argv sys
    text = getPlainTextFromFile(input)
    singleCharDict = getTextStatistics(text)

    treeBuilder = TreeBuilder(singleCharDict)
    treeBuilder.Run()
    coder = Coder(treeBuilder.GetRoot()[0])
    coder.Run()
    msg = coder.code(text)
    print(msg)

    coder.toFile(msg,'outputFile')


if __name__ == "__main__":
    main()




