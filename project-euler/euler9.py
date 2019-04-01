#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:09:58 2019

@author: jisu
"""

def main():
	
	for a in range (1, 1000):
		for b in range(1, 1000):
			for c in range(1, 1000):
				if a+b+c == 1000 and a*a+b*b == c*c:
					print(str(a) + " " + str(b) + " " + str(c))
					return a*b*c

print(str(main()))