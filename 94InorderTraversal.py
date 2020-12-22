#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/18
# Solution: 二叉树前序、中序、后序遍历是针对
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def inorderTraversal(self,root):
        result=[]
        self.helper(root,result)
        return result

    def helper(self,root,res):
        if root!=None:
            if root.left!=None:
                self.helper(root.left,res)
            res.append(root.val)
            if root.right!=None:
                self.helper(root.right,res)

    #非递归，基于栈
    def inorderTraversalV2(self,root):
        result=[]
        stack=[]
        curr=root
        while curr!=None or stack!=[]:
            while curr!=None:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.val)
            curr=curr.right
        return result
    #使用颜色标记该节点是否已访问
    def inorderTraversalV3(self,root):
        WHITE,GRAY=0,1
        res=[]
        stack=[(WHITE,root)]
        while stack:
            color,node=stack.pop()
            if node is None:
                continue
            if color==WHITE:
                stack.append((WHITE,node.right))
                stack.append((GRAY,node))
                stack.append((WHITE,node.left))
            else:
                res.append(node.val)
        return res

    def inorderTraversalV4(self,root):
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
                stack.append(top) #
                stack.append(None) #以下两行的位置绝对了是前序、中序还是后续遍历
                if top.left:
                    stack.append(top.left)
                # 放此位置为前序遍历
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
    print(s.inorderTraversalV4(root))
    pass 