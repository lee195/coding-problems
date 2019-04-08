#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:07:38 2019

@author: jisu
"""
import time


def sleep_then_f(n, f, *args):
	time.sleep(n//1000)
	f(*args)

def main():
	sleep_then_f(1000, print, "ok")
	return 0

main()