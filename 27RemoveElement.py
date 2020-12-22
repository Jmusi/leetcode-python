#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution:

class Solution:
    def removeElement(self,nums,val):
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i

if __name__ == "__main__":

    s=Solution()
    print(s.removeElement([1],1))
    pass 