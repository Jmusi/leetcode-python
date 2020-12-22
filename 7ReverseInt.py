#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/18
# Solution: 数学方案逐步计算，判断是否溢出

class Solution:
    def reverse(self, x):

        result=0
        INT_MAX=2**31-1
        INT_MIN=-2**31
        flag = 1
        while x!=0:
            if x<0:
                x=-x
                flag=-1
            pop= x%10#余数
            x=x//10
            if result > INT_MAX/10 or (result == INT_MAX / 10 and pop > 7):
                return 0
            if result < INT_MIN/10 or (result==INT_MIN/10 and pop<-8):
                return 0
            result=result*10+pop

        return flag*result
    def reverseV2(self,x):
        if x==0:
            return 0
        s=str(x)
        fuhao = ''
        if s.startswith('-'):
            fuhao = '-'
            s=s[1:]
        s=list(s)
        s.reverse()
        s=''.join(s)
        s=fuhao+s.lstrip('0')
        s=int(s)
        if s >= -2**31 and s <=2**31-1:
            return s
        return 0
if __name__ == "__main__":

    s=Solution()
    print(s.reverse(-123))
    pass
