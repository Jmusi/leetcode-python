#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/18
# Solution: flag记录是否到达Z型的转弯处

class Soulution:
    def convert(self,s,numRows):
        if numRows==1:
            return s
        rowchars=["" for _ in range(numRows)]
        i,flag=0,-1
        for c in s:
            rowchars[i]+=c # 第i行加入字符串
            if i == 0 or i == numRows - 1:
                flag = -flag
            i+=flag

        return "".join(rowchars)



if __name__ == "__main__":
    s=Soulution()
    print(s.convert("abdacsersd",3))