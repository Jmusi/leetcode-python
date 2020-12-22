#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/20
# Solution: 方案1是参照twosum的方案，先字典记录两个值的和，然后查找O(n^2),方案2是排序后使用双指针
# 注意去除重复项

class Solution:
    def threeSum(self,nums):
        if not nums or len(nums)<3:
            return []
        result=[]

        sort_num=sorted(nums)
        for i in range(len(sort_num)):
            if sort_num[i]>0:
                return result
            if i>0 and sort_num[i]==sort_num[i-1]:
                continue
            left=i+1
            right=len(sort_num)-1
            while left<right:
                if sort_num[i]+sort_num[left]+sort_num[right]==0:
                    result.append([sort_num[i],sort_num[left],sort_num[right]])
                    while left<right and sort_num[left+1]==sort_num[left]:
                        left+=1
                    while right>left and sort_num[right]==sort_num[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sort_num[i]+sort_num[left]+sort_num[right]>0:
                    right-=1
                else:
                    left+=1
        return result
if __name__ == "__main__":
    s=Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    pass 