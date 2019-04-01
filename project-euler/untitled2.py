#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:01:41 2019

@author: jisu
"""

def main():
	a = 0
	b = 1
	sum = 0
	
	while (b < 4000000):
		a, b = b, a+b
		if b%2 == 0:
			 sum += b
	return sum

print(str(main()))