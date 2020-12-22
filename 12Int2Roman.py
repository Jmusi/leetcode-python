#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/20
# Solution: 从高到底依次循环遍历最适合的符号，知道最终值为0

class Solution:
    symb=[(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    def int2Roman(self, num):
        result=''
        while num>0:
            for n,s in self.symb:
                if num<n:
                    continue
                count,num=divmod(num,n)
                result=result+s*count
        return result


if __name__ == "__main__":
    s=Solution()
    print(s.int2Roman(2999))
    pass 