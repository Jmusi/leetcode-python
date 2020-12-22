#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/4
# Solution:
class Solution:
    def sortColors(self,nums):
        p0=curr=0 #三个指针，对所有idx<p0:nums[idx<p0]=0,curr表示当前元素下标
        p2=len(nums)-1 #nums[idx>p2]=2

        while curr<=p2:
            if nums[curr]==0:
                nums[p0],nums[curr]=nums[curr],nums[p0]
                p0+=1
                curr+=1
            elif nums[curr]==2:
                nums[curr],nums[p2]=nums[p2],nums[curr]
                p2-=1
            else:
                curr+=1
if __name__ == "__main__":
    nums=[2,0,2,1,1,2]
    s=Solution()
    s.sortColors(nums)
    print(nums)
    pass 