#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/9
# Solution:
class Solution:
    def removeDuplicates(self,nums):
        count=1
        j=1#快慢指针，i指向当前遍历的元素，j指向下一个要覆盖的位置
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                count=1
            if count<=2:
                nums[j]=nums[i]
                j+=1
        return j

if __name__ == "__main__":
    s=Solution()
    nums=[1,1,1,2,2,2,3,4]
    print(s.removeDuplicates(nums))
    print(nums)
    pass 