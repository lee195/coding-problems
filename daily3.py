#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:34:48 2019

@author: jisu
"""

class Node:
    
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

		
def serialize(root: Node):
	if root.left == None and root.right == None:
		return root.val
	if root.left == None:
		return str(root.val)+", "+serialize(root.right)
	if root.right == None:
		return serialize(root.left)+", "+str(root.val)
	return serialize(root.left)+", "+str(root.val)+", "+serialize(root.right)


def clean_string(los):
	clean = ""
	for s in los:
		clean += s + ", "
	return clean[:-2]
		

def deserialize(s: str):
	los = str(s).split(", ")
	if len(los) == 1:
		return Node(s, None, None)
	if len(los) == 2:
			return Node(los[1], Node(los[0], None, None), None)
		
	root_val = los[len(los)//2]
	clean_left = clean_string(los[:len(los)//2])
	clean_right = clean_string(los[len(los)//2+1:])

	return Node(root_val, deserialize(clean_left), deserialize(clean_right))


def main():
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	print(serialize(node))
	assert deserialize(serialize(node)).left.left.val == 'left.left'
	
main()