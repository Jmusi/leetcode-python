#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution: 算法复杂度要求在log(n),二分查找

class Solution:
    def search(self,nums,target):
        if not nums:
            return -1
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
if __name__ == "__main__":
    s=Solution()
    print(s.search([4,5,6,7,0,1,2],4))
    pass 