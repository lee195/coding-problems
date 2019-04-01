#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 20:36:10 2019

@author: jisu
"""
import math


def is_prime(n):
	if n == 2:
		return True
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

def sum_of_primes(n):
	return sum([x for x in range(2, n) if is_prime(x)])

def main():
	print(str(sum_of_primes(2000000)))
	return 0
	
main()