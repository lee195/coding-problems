#!/usr/bin/env, python3
#, -*-, coding:, utf-8, -*-
"""
Created, on, Sun, Mar, 31, 2:51:9, 219

@author:, jisu
"""


def read_matrix(matrix):
	with open("grideuler11") as f:
		grid = f.readlines()
		grid = [x.rstrip('\n') for x in grid]
	
	for i, line in enumerate(grid):
		nums = line.split()
		for j, n in enumerate(nums):
			if n[0] == 0:
				n = n[1:]
			matrix[i][j] = int(n)
	return matrix


def calc_right(i, j, matrix):
	tmp = matrix[i, j]
	tmp *= matrix[i, j+1]
	tmp *= matrix[i, j+2]
	tmp *= matrix[i, j+3]
	return tmp

def calc_left(i, j, matrix):
	tmp = matrix[i, j]
	tmp *= matrix[i, j-1]
	tmp *= matrix[i, j-2]
	tmp *= matrix[i, j-3]
	return tmp

def calc_down(i, j, matrix):
	tmp = matrix[i, j]
	tmp *= matrix[i+1, j]
	tmp *= matrix[i+2, j]
	tmp *= matrix[i+3, j]
	return tmp

def calc_up(i, j, matrix):
	tmp = matrix[i, j]
	tmp *= matrix[i-1, j]
	tmp *= matrix[i-2, j]
	tmp *= matrix[i-3, j]
	return tmp

def calc_adj(i, j, matrix):
	largest = 0
	tmp = 1
	if j < 17:
		tmp = calc_right(i, j, matrix)
		if  tmp > largest:
			largest = tmp

	if j > 2:
		tmp = calc_left(i, j, matrix)
		if tmp > largest:
			largest = tmp

	if i < 17:
		tmp = calc_down(i, j, matrix)
		if tmp > largest:
			largest = tmp
	
	if i > 2:
		tmp = calc_up(i, j, matrix)
		if tmp > largest:
			largest = tmp

def main():
	matrix = [[0]*20 for x in range (20)]
	matrix = read_matrix(matrix)
	
	biggest = 1
	
	for i in range(20):
		for j in range(20):
			
	
	return 0

main()