#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/6
# Solution:
class Solution:
    def subsets(self,nums):

        def backtrack(first,curr,k):
            if len(curr)==k:
                result.append(curr[:])
                return
            for i in range(first,len(nums)):
                curr.append(nums[i])
                backtrack(i+1,curr,k)
                curr.pop()
        result=[]
        for k in range(0,len(nums)+1):
            backtrack(0,[],k)
        return result
if __name__ == "__main__":
    s=Solution()
    print(s.subsets([1,2,3]))
    pass 