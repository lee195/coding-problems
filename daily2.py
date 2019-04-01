#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:38:59 2019

@author: jisu
"""

def mul_reduce(l, i):
	res = 1
	for j in range(len(l)):
		if j != i:
			res *= l[j]
	return res

def main():
	initial = [1, 2, 3, 4, 5]
	new = [mul_reduce(initial, x) for x in range(len(initial))]
	
	print(new)
	return True

main()