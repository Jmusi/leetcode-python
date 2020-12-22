#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/23
# Solution:

class Solution:
    INT_MAX=2**31-1
    INT_MIN=-2**31
    def divide(self,dividend,divisor):
        if dividend==0:
            return 0
        if divisor==1:
            return dividend
        if divisor==-1:
            if dividend>self.INT_MIN:
                return -dividend
            return self.INT_MAX
        a=dividend
        b=divisor
        sign=1
        if (a>0 and b<0) or (a<0 and b>0):
            sign=-1
        a=abs(a)
        b=abs(b)
        result=self.div2(a,b)
        if sign>0:
            return min(self.INT_MAX,result)
        else:
            return -result
    def div2(self,a,b):
        if a<b:
            return 0
        count=1
        tb=b
        while tb+tb<=a:
            count=count+count
            tb=tb+tb
        return count + self.div2(a - tb, b)
if __name__ == "__main__":
    s=Solution()
    print(s.divide(10,3))
    pass