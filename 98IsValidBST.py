#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/20
# Solution:
class TreeNode:
    def __init__(self,x):
        self.left=None
        self.right=None
        self.val=x

class Solution:
    #递归
    def isValidBST(self,root):

        def helper(root,lower=float('-inf'),upper=float('inf')):
            if root==None:
                return True
            val=root.val
            if val<=lower or val>=upper:
                return False
            if not helper(root.right,val,upper):
                return False
            if not helper(root.left,lower,val):
                return False
            return True

        return helper(root)
    #中序遍历


if __name__ == "__main__":
    pass 