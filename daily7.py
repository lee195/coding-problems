#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:54:20 2019

@author: jisu
"""

from string import ascii_lowercase

encoding = {}

def pop_encoding():
	for i, c in enumerate(ascii_lowercase):
		encoding[i+1] = c
	return True


def count_encodings(s):
	count = 1
	tmp = 0
	indices = []
	for i in range(0, len(s)-1):
		if int(s[i:i+2]) in encoding:
			tmp += 1
			indices.append(i)
	count += tmp
	tmp = 0
	for i in indices:
		for j in indices:
			if j != i and j - i > 1:
				tmp +=1
	count += tmp
	return count

def main():
	pop_encoding()
	print(encoding)
	print(str(count_encodings('11111')))
	
	return True

main()