from Parser import Parser
from TreeBuilder import TreeBuilder, HoffmanNode


class Coder():
    def __init__(self, treeRoot):
        self.treeRoot = treeRoot
        self.codeDict = {}

    def Run(self):
        self.CodeSingleNode(self.treeRoot, 'x')

    def CodeSingleNode(self, node, code):
        if (node.GetLeft() != None):
            leftCode = code + '0'
            self.CodeSingleNode(node.GetLeft(), leftCode)
        if (node.GetRight() != None):
            rightCode = code + '1'
            self.CodeSingleNode(node.GetRight(), rightCode)
        if (node.GetSymbol() != None):
            self.codeDict[node.GetSymbol()] = code

    def GetSymbolCode(self, symbol):
        return self.codeDict[str(symbol)]

parser = Parser()
parser.Run()
treeBuilder = TreeBuilder(parser.GetDict('1'))
treeBuilder.Run()
coder = Coder(treeBuilder.GetRoot()[0])
coder.Run()
print(coder.GetSymbolCode('d'))


