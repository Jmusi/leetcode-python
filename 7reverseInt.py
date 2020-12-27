#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/12/27
# Solution:
def reverse(x):
    str_x=str(x)
    flag=1
    if x<0:
        flag=-1
        str_x=str_x[1:]
    str_x=str_x[::-1]
    result= flag*int(str_x)
    if result>=-2**31 and result<=2**31-1:
        return result
    return 0
if __name__ == "__main__":
    print(reverse(0))
    pass 