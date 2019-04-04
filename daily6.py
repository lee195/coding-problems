#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:38:24 2019

@author: jisu
"""

memory = {}


class Node:
	def __init__(self, mem_ptr, val):
		self.mem_ptr = mem_ptr
		self.ptr = 0
		self.val = val
		memory[mem_ptr] = self
	
	def __repr__(self):
		return "[" + str(self.ptr) + " , " + str(self.val) + "]"
	

class Linkedxor:
	def __init__(self, first: Node):
		self.first = first
	
	def add(self, element: Node):
		current = self.first
		prev_ptr = 0
		while(current.ptr ^ prev_ptr != 0):
			tmp = current.mem_ptr
			current = memory[prev_ptr ^ current.ptr]
			prev_ptr = tmp

		current.ptr = current.ptr ^ element.mem_ptr
		element.ptr = element.ptr ^ current.mem_ptr
		
		return True
	
	def get(self, index):
		current = self.first
		prev_ptr = 0
		for i in range(index):
			tmp = current.mem_ptr
			current = memory[current.ptr ^ prev_ptr]
			prev_ptr = tmp
		return current
			
def main():
	n0 = Node(1, 'a')
	n1 = Node(2, 'b')
	n2 = Node(3, 'c')
	n3 = Node(4, 'd')
	
	xorl = Linkedxor(n0)
	print(memory)
	xorl.add(n1)
	print(memory)
	xorl.add(n2)
	print(memory)
	xorl.add(n3)
	print(memory)
			
	for i in range(4):
		print(xorl.get(i))
		
	return 0

main()