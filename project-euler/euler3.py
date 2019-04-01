#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:24:54 2019

@author: jisu
"""
from math import sqrt

def prime(n):
	upper_bound = int(sqrt(n))+1
	for i in range(2, upper_bound):
		if n%i == 0:
			return False
	return True

def factorization(n):
	upper_bound = int(sqrt(n))+1
	return [x for x in range(2, upper_bound) if prime(x) and n%x == 0]
	
def main():
	print(factorization(600851475143))
	return True

main()