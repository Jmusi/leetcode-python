#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/26
# Solution: 字符串相乘https://leetcode-cn.com/problems/multiply-strings/solution/gao-pin-mian-shi-xi-lie-zi-fu-chuan-cheng-fa-by-la/
class Solution:
    def multiply(self,num1,num2):
        m=len(num1)
        n=len(num2)
        res=[0 for _ in range(m+n)] #m位数乘以n位数结果最多为m+n位数
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul=int(num1[i])*int(num2[j])
                #乘积结果保存在res的对应位置
                p1=i+j
                p2=i+j+1
                sum=mul+res[p2]
                res[p2]=sum%10
                res[p1]+=sum//10
        #去除开头的0
        i=0
        while i<len(res) and res[i]==0:
            i+=1
        result_str=''
        while i<len(res):
            result_str+=str((res[i]))
            i+=1
        return '0' if len(result_str)==0 else result_str

if __name__ == "__main__":
    s=Solution()
    print(s.multiply('1234567','2345'))
    pass 