#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/14
# Solution: 依次计算n=1,n=2...
class Solution:
    def grayCode(self,n):
        res,head=[0],1
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(head+res[j])
            head<<=1
        return res
if __name__ == "__main__":
    s=Solution()
    print(s.grayCode(2))
    pass 