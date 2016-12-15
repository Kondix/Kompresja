import sys as system
import FileReader as fr

class Parser:
    def __init__(self):
        reader = fr.FileReader(system.argv[1])
        self.data = reader.data
        self.letterStatistic = reader.CountCharactersInData()
        self.minWindowSize = 1
        self.maxWindowSize = 2
        self.dataDictList = {}

    def Run(self):
        for windSize in range (self.minWindowSize, self.maxWindowSize + 1):
            dataDict = Counter()
            dataChunks = [self.data[i:i + windSize] for i in range(0, len(self.data), windSize)]
            for dataChunk in dataChunks:
                self.__IncrementDict(dataChunk, dataDict, windSize)
            self.dataDictList[str(windSize)] = dataDict

    def __IncrementDict(self, dataChunk, dataDict, windSize):
        dataDict[dataChunk] += 1

    def PrintDict(self):
        print(self.dataDictList)

    def GetDict(self):
        return self.dataDictList

    def GetDict(self, idx):
        return self.dataDictList[str(idx)]

class Counter(dict):
    def __missing__(self, key):
         return 0

