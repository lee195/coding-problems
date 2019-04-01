#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:21:50 2019

@author: jisu
"""

def main():
	square_sum = sum([x for x in range(101)])**2
	print(str(square_sum))
	squared_sum = sum([x*x for x in range(101)])
	print(str(squared_sum))
	
	return abs(square_sum - squared_sum)

print(str(main()))