#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:14:14 2019

@author: jisu
"""
		

class Node:
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right
	
	def __repr__(self):
		return str(self.val)
	
def check_unival(root: Node):
	if root.left == None and root.right == None:
		return True
	if root.val != root.left.val or root.val != root.right.val:
		return False
	return check_unival(root.left) and check_unival(root.right)
	

def list_nodes(root:Node):
	
	if root == None:
		return []
	
	return [root] + list_nodes(root.left) + list_nodes(root.right)


def count_univals(root: Node):
	return sum([1 for x in list_nodes(root) if check_unival(x)])

	
if __name__ == "__main__":
	node1 = Node(1, None, None)
	node2 = Node(1, None, None)
	
	node3 = Node(1, node1, node2)
	node4 = Node(0, None, None)
	
	node5 = Node(1, None, None)
	node6 = Node(0, node3, node4)
	
	node7 = Node(0, node5, node6)
	
	print(str(count_univals(node7)))

	