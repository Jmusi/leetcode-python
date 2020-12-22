#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/28
# Solution:
class Solution:
    def myPow(self,x,n):
        #递归，快速幂运算，x^16->x^8*x^8->x^4*x^4...避免重复计算
        def quickMul(N):
            if N==0:
                return 1
            y=quickMul(N//2)
            return y*y if N%2==0 else y*y*x
        return quickMul(n) if n>=0 else 1/(quickMul(-n))

if __name__ == "__main__":
    s=Solution()
    print(s.myPowV2(2,-1))
    pass 