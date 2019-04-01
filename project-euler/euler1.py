#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:54:23 2019

@author: jisu
"""

def main():
	mul3_5 = [x for x in range (1000) if x%3 == 0 or x%5 == 0]
	return sum(mul3_5)

print(str(main()))