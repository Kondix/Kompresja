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
	statistics.update({symbols[i]:numbers[i]})

print(statistics)

treeBuilder = TreeBuilder(statistics)
treeBuilder.Run()

decoderDict = {}

coder = Coder(treeBuilder.GetRoot()[0])
coder.Run()


for symbol in symbols:
	print(symbols)
	seq = coder.codeSingle(symbol)
	decoderDict.update({seq:symbol})

with open('ostatecznyOutput.bin') as x:
	binaryStream = unpack('<i', bytearray(x.read(4)))

