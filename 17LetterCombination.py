#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/21
# Solution:
class Solution:
    num2char={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    def letterCombination(self,digits):
        if '0' in digits or '9' in digits or len(digits)<=0:
            return []

        results=list(self.num2char.get(digits[0]))
        for i in range(1,len(digits)):
            ser=self.num2char.get(digits[i])
            new_result=[]
            for r in results:
                r=[r+s for s in ser]
                new_result.extend(r)
            results=new_result
        return results

    # 回溯
    def letterCombinationV2(self,digits):
        dd = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        rst = []
        if not digits: return rst

        def dfs(curr, location, digits):
            if location == len(digits):
                rst.append(curr)
            else:
                for i in dd[digits[location]]:
                    dfs(curr + i, location + 1, digits)

        dfs("", 0, digits)
        return rst
if __name__ == "__main__":
    s=Solution()
    print(s.letterCombinationV2('234'))
    pass 