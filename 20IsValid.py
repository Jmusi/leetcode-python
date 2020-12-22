#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/22
# Solution:
class Solution:
    def isValid(self,s):
        if s=='':
            return True
        result=[]
        try:
            for c in s:
                if c=='}' and result[-1]=='{':
                    result=result[:-1]
                elif c==')' and result[-1]=='(':
                    result=result[:-1]
                elif c==']' and result[-1]=='[':
                    result=result[:-1]
                else:
                    result.append(c)
        except:
            return False
        if len(result)>0:
            return False
        return True
    def isValidV2(self,s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == "__main__":
    s=Solution()
    print(s.isValid('([)]'))
    pass 