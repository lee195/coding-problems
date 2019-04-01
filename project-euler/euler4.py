#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:37:41 2019

@author: jisu
"""

def is_palindrome(n):
	return str(n) == str(n)[::-1]

def main():
	largest = 0
	for a in range (999, 100, -1):
		for b in range (999, 100, -1):
			if is_palindrome(a*b) and len(str(a*b)) >= len(str(largest)) and a*b > largest:
				largest = a*b
	print(str(largest))
	return True

main()