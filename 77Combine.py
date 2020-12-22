#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/6
# Solution:
class Solution:
    def combine(self,n,k):
        result=[]
        used={}
        # first开始位置，curr已选数字
        def backtrack(first=1,curr=[]):
            if len(curr)==k:
                result.append(curr[:])
                return
            # first是递归传进来的起始位置，否则每次从0开始会出现[1,2]和[2,1]重复
            for i in range(first,n+1):
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()

        backtrack(1,[])
        return result
if __name__ == "__main__":
    s=Solution()
    print(s.combine(4,2))
    pass 