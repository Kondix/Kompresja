from TreeBuilder import TreeBuilder, HoffmanNode
from temp import *
import binascii
import time
from struct import unpack
from Coder import Coder
import os

with open("newSymbol.txt") as x:
	symbolContent = x.read()
with open("newNumber.txt") as x:
	numberContent = x.read()

statistics = {}

symbols = symbolContent[:-1].split('†')
numbers = numberContent[:-1].split('†')
for i in range(len(symbols)):
	statistics.update({symbols[i]:int(numbers[i])})

treeBuilder = TreeBuilder(statistics)
treeBuilder.Run()

decoderDict = {}

coder = Coder(treeBuilder.GetRoot()[0])
coder.Run()

coder.printCodeDict()

for symbol in symbols:
	seq = coder.codeSingle(symbol)
	decoderDict.update({seq:symbol})

with open('outputFile1.bin', encoding = "ISO-8859-1") as file:
	content = file.read()
	b = bytearray(content.encode(encoding = "ISO-8859-1"))
	out = ''
	for idx in range(0, len(content)-5, 4):
		binaryStream = unpack('<i', b[idx:idx+4])
		binaryString= str((bin(binaryStream[0]).replace("-", '').replace("0b", '')))
		match = '';
		for a in binaryString:
			match += a
			if match in coder.getCodeDict().values():
				for el in coder.getCodeDict():
					if coder.getCodeDict()[el] == match:
						out += el
				match = ''

	print(out)

