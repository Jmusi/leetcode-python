#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/14
# Solution:
class Solution:
    def merge(self,nums1,m,nums2,n):
        i=m-1
        j=n-1
        k=n+m-1 #nums1的结束位置
        while i>=0 and j>=0:
            if nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        # 重要！！！！
        nums1[:j+1]=nums2[:j+1]
if __name__ == "__main__":
    s=Solution()
    nums1=[1,2,3,0,0,0]
    nums2=[2,5,6]
    s.merge(nums1,3,nums2,3)
    print(nums1)
    pass 