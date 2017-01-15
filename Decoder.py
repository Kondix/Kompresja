from TreeBuilder import TreeBuilder
from struct import unpack
from Coder import Coder

class Decoder:
	def __init__(self, symbolFile, numberFile, coder = None):
		self.out = ''
		if (coder == None):
			self.symbolContent = open(symbolFile).read()
			self.numberContent = open(numberFile).read()
			self.statistics = {}
			self.UpdateStatistics()
			self.BuildCode()
		else:
			self.coder = coder

	def Run(self):
		self.UpdateStatistics()

	def UpdateStatistics(self):
		symbols = self.symbolContent[:-1].split('†')
		numbers = self.numberContent[:-1].split('†')
		for i in range(len(symbols)):
			self.statistics.update({symbols[i]: int(numbers[i])})

	def BuildCode(self):
		treeBuilder = TreeBuilder(self.statistics)
		treeBuilder.Run()
		self.coder = Coder(treeBuilder.GetRoot()[0])
		self.coder.Run()

	def DecodeFile(self, fileToDecode):
		with open(fileToDecode, encoding="ISO-8859-1") as file:
			content = bytearray(file.read().encode(encoding="ISO-8859-1"))
			return (self.Decode(content))

	def Decode(self, input):
		self.out = ''
		match = ''
		for idx in range(0, len(input) - 5, 4):
			binaryString = str((bin(unpack('<i', input[idx:idx + 4])[0]).replace("-", '').replace("0b", '')))
			#paddingLen = 32 - (len(binaryString) % 32)
			#padding = '0' * paddingLen
			#binaryString = binaryString + padding
			for a in binaryString:
				match += a
				if match in self.coder.getCodeDict().values():
					for el in self.coder.getCodeDict():
						if self.coder.getCodeDict()[el] == match:
							self.out += el
					match = ''
		return self.out

	def DecodeString(self, input):
		self.out = ''
		match = ''
		for sign in input:
			match += sign
			if match in self.coder.getCodeDict().values():
				for el in self.coder.getCodeDict():
					if self.coder.getCodeDict()[el] == match:
						self.out += el
				match = ''
		return self.out

	def DecodeAllLevelsString(self, input, transNodes = {}):
		self.out = ''
		match = ''
		for sign in input:
			match += sign
			if match in self.coder.getCodeDict().values():
				for element in self.coder.getCodeDict():
					if self.coder.getCodeDict()[element] == match:
						if element in transNodes.keys():
							self.RecurencyDecode(element, transNodes)
				match = ''
		return self.out

	def RecurencyDecode(self, input, transNodes):
		for element in input:
			if element in transNodes.keys():
				self.RecurencyDecode(transNodes[element], transNodes)
			else:
				self.out += element


#decoder = Decoder("newSymbol.txt", "newNumber.txt")
#print(decoder.DecodeFile("ostatecznyOutput.bin"))
