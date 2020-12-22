#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/26
# Solution: 使用索引作为哈希键 以及元素的符号作为哈希值 来实现是否存在的检测。
# 例如，nums[2] 元素的负号意味着数字 2 出现在 nums 中。nums[3]元素的正号表示 3 没有出现在 nums 中。
# 第一次遍历替换元素中的负数为1，第二次遍历将数字对应位置的数值改为负数，第三次遍历第一个为正数的元素下标即为结果

class Solution:
    def firstMissingPositive(self,nums):
        if 1 not in nums:
            return 1
        n=len(nums)
        if n==1:
            return 2
        for i in range(n):
            # 结果最大只可能为n+1
            if nums[i]<=0 or nums[i]>n:
                nums[i]=1
        for i in range(len(nums)):
            a=abs(nums[i])
            nums[a-1]=-abs(nums[a-1])
        for i in range(1,n):
            if nums[i]>0:
                return i+1
        return n+1

if __name__ == "__main__":
    s=Solution()
    print(s.firstMissingPositive([3,4,-1,1]))
    pass 