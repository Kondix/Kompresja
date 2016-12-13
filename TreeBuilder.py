from Parser import Parser

import collections

class TreeBuilder:
    def __init__(self, dict):
        self.dictToCode = collections.OrderedDict(sorted(dict.items(), key=lambda dict: dict[1], reverse=True))
        self.nodeList = []

    def Run(self):
        self.CreateBasicTree()
        while (len(self.nodeList) != 1):
            self.__MergeTwoNodesWithLessProbabilty()

    def CreateBasicTree(self):
        for singleDict in self.dictToCode.items():
            self.nodeList.append(HoffmanNode(singleDict[0], singleDict[1]))

    def __MergeTwoNodesWithLessProbabilty(self):
        firstNode = self.nodeList[-1]
        secondNode = self.nodeList[-2]
        newProb = firstNode.GetProb() + secondNode.GetProb()
        self.nodeList.insert(self.__FindPlaceToInsertNewTree(newProb), HoffmanNode(None, newProb, secondNode, firstNode))
        self.nodeList.remove(firstNode)
        self.nodeList.remove(secondNode)

    def __FindPlaceToInsertNewTree(self, prob):
        cnt = 0;
        for node in self.nodeList:
            if node.GetProb() > prob:
                cnt += 1
            else:
                break
        return cnt

    def GetRoot(self):
        return self.nodeList

class HoffmanNode:
    def __init__(self, symbol, prob, right = None, left = None):
        self.symbol = symbol
        self.prob = prob
        self.rightLeaf = right
        self.leftLeaf = left

    def GetProb(self):
        return self.prob

    def GetSymbol(self):
        return self.symbol

    def GetLeft(self):
        return self.leftLeaf

    def GetRight(self):
        return self.rightLeaf
