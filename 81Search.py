#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/9
# Solution:
class Solution:
    def search(self,nums,target):
        if len(nums)==0:
            return False
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[left]:
                left+=1
                continue
            #前半部分有序
            if nums[left]<nums[mid]:
                if nums[mid]>target and nums[left]<=target:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1
        return False
if __name__ == "__main__":
    s=Solution()
    print(s.search([2,5,6,0,0,1,2],0))
    pass 