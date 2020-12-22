#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/18
# Solution:
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def preorderTraversal(self,root):
        result=[]
        self.helper(root,result)
        return result
    def helper(self,root,result):
        if root!=None:
            result.append(root.val)
            if root.left!=None:
                self.helper(root.left,result)
            if root.right!=None:
                self.helper(root.right,result)

    def preorderTraversalV2(self,root):
        if root==None:
            return []
        #使用一个标注区分
        res=[]
        stack=[root]
        while stack!=[]:
            top=stack.pop()
            if top!=None:
                # 放此位置为后序遍历
                if top.right:
                    stack.append(top.right)
                # 放此位置为中序遍历
                if top.left:
                    stack.append(top.left)
                stack.append(top) #
                stack.append(None) #以下两行的位置绝对了是前序、中序还是后续遍历

            else:
                res.append(stack.pop().val)
        return res
if __name__ == "__main__":
    root=TreeNode(2)
    rl=TreeNode(1)
    rr=TreeNode(3)
    root.left=rl
    root.right=rr
    s=Solution()
    print(s.preorderTraversalV2(root))
    pass 