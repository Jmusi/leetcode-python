#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution: left和right分别记录左右括号的数量,回溯法

class Solution:
    def generateParenthesis(self,n):
        result=[]
        def backtrack(s,left,right):
            if len(s)==2*n:
                result.append(''.join(s))
                return
            if left<n:
                s.append('(')
                backtrack(s,left+1,right)
                s.pop()
            if right<left:
                s.append(')')
                backtrack(s,left,right+1)
                s.pop()
        backtrack([],0,0)
        return result

if __name__ == "__main__":
    s=Solution()
    print(s.generateParenthesis(3))
    pass 