#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/19
# Solution: 自己实现字符串转int函数

class Solution:
    def myAtoI(self,s):
        s=s.lstrip()
        flag=1
        if s=='':
            return 0
        if s[0]=='-':
            s=s[1:]
            flag=-1
        elif s[0]=='+':
            s=s[1:]
        result=0
        for c in s:
            if c.isdigit():
                result=result*10+int(c)
            else:
                break
        if result*flag>2**31-1:
            return 2**31-1
        elif result*flag<-2**31:
            return -2**31
        else:
            return result*flag
if __name__ == "__main__":
    s=Solution()
    print(s.myAtoI('+-12 '))
    pass 