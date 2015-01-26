#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)

root.left = left
root.right = right

print root
