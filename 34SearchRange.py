#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution:
class Solution:
    def searchRange(self,nums,target):
        if nums==None or len(nums)==0:
            return [-1,-1]
        left_index=self.search(nums,target,True)
        if left_index==len(nums) or nums[left_index]!=target:
            return [-1,-1]

        return [left_index,self.search(nums,target,False)-1]
    #二分查找,不小于target的最左测位置
    def search(self,nums,target,left):
        lo=0
        hi=len(nums)
        while lo<hi:
            mid=(lo+hi)//2
            # 最左的位置
            if nums[mid]>target or (left and target==nums[mid]):
                hi=mid
            else:
                lo=mid+1
        return lo
if __name__ == "__main__":
    s=Solution()
    print(s.searchRange([1,2,3,3,4,4,5,6],3))
    pass 