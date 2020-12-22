#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/16
# Solution:

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]==target:
                    return [i,j]

    #在第一次迭代中，我们将每个元素的值和它的索引添加到表中。
    # 然后，在第二次迭代中，我们将检查每个元素所对应的目标元素（target - nums[i]target−nums[i]）
    # 是否存在于表中。注意，该目标元素不能是 nums[i]nums[i] 本身！

    def twoSumV2(self,nums, target):
        num_index={}
        for i in range(len(nums)):
            num_index[nums[i]]=i

        for i in range(len(nums)):
            a=nums[i]
            b=num_index.get(target-a)

            if b and b!=i:
                return [i,b]

    def twoSumV3(self,nums,target):
        num_index={}
        for i in range(len(nums)):
            a=nums[i]
            b=num_index.get(target-a)
            if b!=None:
                return [i,b] if i<b else [b,i]
            else:
                num_index[a]=i

if __name__ =='__main__':
    s=Solution()
    nums=[-3,4,3,90]
    target=0

    print(s.twoSum(nums,target))
    print(s.twoSumV2(nums,target))
    print(s.twoSumV3(nums,target))
