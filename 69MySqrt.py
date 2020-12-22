#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/1
# Solution: 只取整数位，而不是四舍五入
class Solution:
    def mySqrt(self,x):
        left=0
        right=x
        result=-1
        while left<=right:
            mid=(left+right)//2
            tmp=mid*mid
            if tmp<=x:
                result=mid
                left=mid+1
            else:
                right=mid-1
        return result
if __name__ == "__main__":
    s=Solution()
    print(s.mySqrt(7))
    pass 