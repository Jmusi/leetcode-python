#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/1
# Solution:
class Solution:
    def addBinary(self,a,b):
        result=[]
        m=len(a)
        n=len(b)
        #较短的字符串前面补0，使得长度相等
        if m<n:
            a='0'*(n-m)+a
        else:
            b='0'*(m-n)+b
        i=len(a)-1
        carry='0'
        while i>=0:
            if a[i]=='1' and b[i]=='1':
                result.append(carry)
                carry='1'
            elif a[i]=='0' and b[i]=='0':
                result.append(carry)
                carry='0'
            else:
                if carry=='0':
                    result.append('1')
                else:
                    result.append('0')
                    carry='1'
            i-=1
        if carry=='1':
            result.append('1')
        result.reverse()
        return ''.join(result)
if __name__ == "__main__":
    s=Solution()
    print(s.addBinary('1010','1011'))
    pass 