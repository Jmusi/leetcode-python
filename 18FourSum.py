#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/21
# Solution:
class Solution:
    def fourSum(self,nums,target):
        if nums==None or len(nums)<4:
            return []
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j] == nums[j - 1]:
                    continue
                left=j+1
                right=len(nums)-1
                while(left<right):
                    tmp=nums[i]+nums[j]+nums[left]+nums[right]
                    if tmp==target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while right > left and nums[right - 1] == nums[right]:
                            right -= 1
                        left+=1
                        right-=1
                    elif tmp>target:
                        right-=1
                    else:
                        left+=1

        return result

if __name__ == "__main__":
    s=Solution()
    print(s.fourSum([0,0,0,0],0))
    pass 