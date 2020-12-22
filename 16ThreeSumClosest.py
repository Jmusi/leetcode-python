#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/21
# Solution:
class Solution:
    def threeSumClosest(self,nums,target):
        if not nums or len(nums)<3:
            return None

        sort_nums=sorted(nums)
        cur_min=sort_nums[0]+sort_nums[1]+sort_nums[2]
        for i in range(len(sort_nums)):
            left=i+1
            right=len(sort_nums)-1
            while left<right:
                cur_sum=sort_nums[i]+sort_nums[left]+sort_nums[right]
                cur_dist=abs(cur_sum-target)
                if cur_dist<abs(cur_min-target):
                    cur_min=cur_sum
                if cur_sum>target:
                    right-=1
                elif cur_sum<target:
                    left+=1
                else:
                    return target
        return cur_min

if __name__ == "__main__":
    s=Solution()
    print(s.threeSumClosest([-1,2,1,-4],1))
    pass
