#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution:从后往前寻找第一个升序对(i,j)即nums[i]<nums[j] 再从后往前找第一个大于nums[i]的数即为大数，交换着两个元素即将大数换到前面，然后将大数后面的部分倒序

class Solution:
    def nextPermutation(self,nums):
        n = len(nums)
        if n<2: return nums
        i = n-1
        while i>0 and nums[i-1]>=nums[i]:#要是前者大于等于后者 则不是要调整的目标 继续前移  ！第一遍出错就是这儿没有等于
            i -= 1
        if i==0 and nums[i]==max(nums): #此数为最大数
            return nums.reverse()
        else:
            j = n-1
            while j>i-1 and nums[j]<=nums[i-1]:
                j -= 1
            nums[i-1],nums[j]=nums[j],nums[i-1]
            re = nums[i:]
            for h in range (len(re)):
                nums[n-1-h] = re[h]
            return nums
if __name__ == "__main__":
    s=Solution()
    print(s.nextPermutation([1,3,2]))
    pass 