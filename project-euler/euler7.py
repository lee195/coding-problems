#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:41:27 2019

@author: jisu
"""

import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
		
	return True

def nth_prime(n):
	count = 0
	candidate = 2
	while count < n:
		if is_prime(candidate):
			print(str(candidate))
			count += 1
		candidate += 1
	return candidate-1

def main():
	print("starting")
	print(str(nth_prime(10001)))
	
main()