#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution:
class Solution:
    def removeDuplicates(self,nums):
        prev=0 #记录上一个唯一数据的位置
        for i in range(1,len(nums)):
            if nums[i]==nums[prev]:
                continue
            prev+=1
            nums[prev]=nums[i]
        nums=nums[:prev+1]
        return prev+1

if __name__ == "__main__":
    s=Solution()
    s.removeDuplicates([1,1,3,4,4,5])
    pass 