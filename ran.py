#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Protocol.KDF import PBKDF1
from hamming import hammingDistance
import os

def sbin (s1):
	return ''.join('{0:08b}'.format(int(x, 16)) for x in (s1.encode("hex")[i:i+2] for i in xrange(0, len(s1.encode("hex")), 2)))

def hamming2(s1,s2):
	s1bin = sbin(s1)
	s2bin = sbin(s2)
	return hammingDistance(s1bin,s2bin)

if __name__ == '__main__':
	N = 1000000
	while N>0:
		try:
			s1 = os.urandom(20)
			s2 = os.urandom(20)
			print hamming2(s1,s2)
			N = N-1
		except:
			pass

'''generador de numeros aleatorios
distancia de hamming '''
