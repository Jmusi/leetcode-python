#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/1
# Solution:
class Solution:
    def plusOne(self,digits):
        if digits==[]:
            return [1]
        result=[]
        last_num=digits[-1]+1
        carry=last_num//10
        new_v=last_num%10
        result.append(new_v)
        for i in range(len(digits)-2,-1,-1):
            v=digits[i]+carry
            result.append(v%10)
            carry=v//10
        if carry!=0:
            result.append(carry)
        result.reverse()
        return result
    def plusOneV2(self,digits):
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=1
            digits[i]=digits[i]%10
            if digits[i]!=0:
                return digits
        digits=[1]+digits
        return digits
if __name__ == "__main__":
    s=Solution()
    print(s.plusOneV2([9,9,9]))
    pass 