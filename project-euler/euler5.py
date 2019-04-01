#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:16:17 2019

@author: jisu
"""

def is_div(n):
	for i in range(1, 20):
		if n%i != 0:
			return False
	return True

def main():
	n = 20
	while(not is_div(n)):
		n += 20
	
	return n

print(str(main()))