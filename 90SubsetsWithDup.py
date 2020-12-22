#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/15
# Solution: #与78题区别在于重复判断
class Solution:
    def subsetsWithDup(self,nums):
        result=[]
        def backtrace(first,cur,k):
            if len(cur)==k:
                result.append(cur[:])
                return
            for i in range(first,len(nums)):
                #i>first很重要，表示同一层不能重复，但是不同递归层可以重复，比如[1,2,2]和[2,2]
                if i>first and nums[i]==nums[i-1]:
                    continue
                cur.append(nums[i])
                backtrace(i+1,cur,k)
                cur.pop()

        nums.sort()
        for k in range(0,len(nums)+1):
            backtrace(0,[],k)
        return result
if __name__ == "__main__":
    s=Solution()
    print(s.subsetsWithDup([1,2,2]))
    pass 