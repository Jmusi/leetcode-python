#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution:
class Solution:
    def searchInsert(self,nums,target):
        if nums==None or len(nums)==0:
            return 0
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left
if __name__ == "__main__":
    s=Solution()
    print(s.searchInsert([1,3,5,6],0))
    pass 