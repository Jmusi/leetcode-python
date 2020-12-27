#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/27
# Solution:
'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
'''

def convert(s,numRows):
    if numRows==1:
        return s
    result=['' for _ in range(numRows)]
    i,flag=0,1
    for c in s:
        result[i]+=c
        if i==numRows-1:
            flag=-1
        if i==0:
            flag=1
        i+=flag
    return ''.join(result)
if __name__ == "__main__":
    print(convert('LEETCODEISHIRING',3))
    pass 