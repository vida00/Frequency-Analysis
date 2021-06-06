#!/bin/env python2

import sys
from string import uppercase as upc

freqEn = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
freqDic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

def main(file):

	file = open(file, 'r').read().upper()
	for line in file:
		if line in upc:
			freqDic[line] += 1

	order = []
	pts = 0

	for word in sorted(freqDic, key=freqDic.get, reverse=True):
		print word, freqDic[word]
		order.append(word)
	
	order = ''.join(order)

	for clt in freqEn[:6]:
		if clt in order[:6]:
			pts += 1

	for ult in freqEn[-6:]:
		if ult in order[-6:]:
			pts +=1
	print 'Score:',pts, 'para 12'

if len(sys.argv) != 2:
	print "Modo de uso: {} message.txt".format(sys.argv[0])
else:
	main(sys.argv[1])
