#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:38:45 2019

@author: jisu
"""

import inspect


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
	loc, _, _, _ = inspect.getclosurevars(pair)
	
	return loc['a']


def cdr(pair):
	loc, _, _, _ = inspect.getclosurevars(pair)
	
	return loc['b']

def main():
	p = cons(3, 4)
	print(str(car(p)))
	print(str(cdr(p)))
	return True

main()