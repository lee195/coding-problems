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
	tmp = matrix[i][j]
	tmp *= matrix[i][j+1]
	tmp *= matrix[i][j+2]
	tmp *= matrix[i][j+3]
	return tmp

def calc_left(i, j, matrix):
	tmp = matrix[i][j]
	tmp *= matrix[i][j-1]
	tmp *= matrix[i][j-2]
	tmp *= matrix[i][j-3]
	return tmp

def calc_down(i, j, matrix):
	tmp = matrix[i][j]
	tmp *= matrix[i+1][j]
	tmp *= matrix[i+2][j]
	tmp *= matrix[i+3][j]
	return tmp

def calc_up(i, j, matrix):
	tmp = matrix[i][j]
	tmp *= matrix[i-1][j]
	tmp *= matrix[i-2][j]
	tmp *= matrix[i-3][j]
	return tmp

def calc_right_down(i, j, matrix):
	tmp = matrix[i][j]
	tmp *= matrix[i+1][j+1]
	tmp *= matrix[i+2][j+2]
	tmp *= matrix[i+3][j+3]
	return tmp

def calc_right_up(i, j, matrix):
	tmp = matrix[i][j]
	tmp *= matrix[i-1][j+1]
	tmp *= matrix[i-2][j+2]
	tmp *= matrix[i-3][j+3]
	return tmp

def calc_left_down(i, j, matrix):
	tmp = matrix[i][j]
	tmp *= matrix[i+1][j-1]
	tmp *= matrix[i+2][j-2]
	tmp *= matrix[i+3][j-3]
	return tmp

def calc_left_up(i, j, matrix):
	tmp = matrix[i][j]
	tmp *= matrix[i-1][j-1]
	tmp *= matrix[i-2][j-2]
	tmp *= matrix[i-3][j-3]
	return tmp

def check_largest(largest, candidate):
	if candidate > largest:
		return candidate
	return largest

def calc_adj(i, j, matrix):
	largest = 0

	if j < 17:
		largest = check_largest(calc_right(i, j, matrix), largest)
		
	if j < 17 and i < 17:
		largest = check_largest(calc_right_down(i, j, matrix), largest)
			
	if j < 17 and i > 2:
		largest = check_largest(calc_right_up(i, j, matrix), largest)
			
	if j > 2:
		largest = check_largest(calc_left(i, j, matrix), largest)
	
	if j > 2 and i < 17:
		largest = check_largest(calc_left_down(i, j, matrix), largest)
		
	if j > 2 and i > 2:
		largest = check_largest(calc_left_up(i, j, matrix), largest)

	if i < 17:
		largest = check_largest(calc_down(i, j, matrix), largest)
	
	if i > 2:
		largest = check_largest(calc_up(i, j, matrix), largest)
			
	return largest

def main():
	matrix = [[0]*20 for x in range (20)]
	matrix = read_matrix(matrix)
	
	biggest = 1
	index_i = 0
	index_j = 0
	
	for i in range(20):
		for j in range(20):
			tmp = calc_adj(i, j, matrix)
			if tmp > biggest:
				biggest = tmp
				index_i = i
				index_j = j
	print("largest found at: " + str(index_i) + ", " + str(index_j))
	print("largest value: " + str(biggest))
	return 0

main()