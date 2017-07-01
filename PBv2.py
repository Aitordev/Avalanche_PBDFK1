#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Protocol.KDF import PBKDF1
from hamming import hammingDistance
import os


def sxor(s1,s2):    
    return ''.join('0' if i == j else '1' for i, j in zip(s1,s2))
def sbin (s1):
	return ''.join('{0:08b}'.format(int(x, 16)) for x in (s1.encode("hex")[i:i+2] for i in xrange(0, len(s1.encode("hex")), 2)))

def hamming2(s1,s2):
	s1bin = sbin(s1)
	s2bin = sbin(s2)
	return hammingDistance(s1bin,s2bin)

if __name__ == '__main__':
	N = 1000000
	salt = os.urandom(8)
	while N>0:
		try:
			password = os.urandom(4)
			result = PBKDF1(password,salt,20)
			passwordbin = sbin(password)
			passwordbin = sxor(password,'10000000000000000000000000000000')
			passwordhex = '%08X' % int(passwordbin,2)
			password = passwordhex.decode("hex")
			result1 = PBKDF1(password,salt,20)
			print hamming2(result,result1)
			N = N-1
		except:
			pass

'''variando un bit al salt
distancia de hamming '''

