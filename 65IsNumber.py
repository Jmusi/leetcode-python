#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/1
# Solution:
class Solution:
    def isNumber(self,s):
        s = s.strip()
        numbers = [str(i) for i in range(10)]
        n = len(s)

        e_show_up, dot_show_up, num_show_up, num_after_e = False, False, False, False

        for i in range(n):
            c = s[i]
            if c in numbers:
                num_show_up = True
                num_after_e = True
            elif c in ('+', '-'):
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif c == '.':
                if dot_show_up or e_show_up:
                    return False
                dot_show_up = True
            elif c == 'e':
                if e_show_up or not num_show_up:
                    return False
                e_show_up = True
                num_show_up = False
            else:
                return False

        return num_show_up and num_after_e

if __name__ == "__main__":
    pass 