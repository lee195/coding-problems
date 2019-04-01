#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:45:49 2019

@author: jisu
"""
import math


def calc_num_div(n):
	count = 2
	
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			if n/i == i:
				count += 1
			count += 2
	
	return count

def main():
	count = 1
	current = 0
	num_div = 0
	
	while num_div < 501:
		current += count
		num_div = calc_num_div(current)
		count += 1
	
	print(str(current))
	return True

main()