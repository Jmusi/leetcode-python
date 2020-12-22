#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution: 康托展开，逆康托展开https://leetcode-cn.com/problems/permutation-sequence/solution/ni-kang-tuo-zhan-kai-xiang-jie-by-boille/
class Solution:
    def getPermutation(self,n,k):
        fact = [1] * (n + 1)  # 多一个 0 的阶乘
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i
        k -= 1  # 对应康托展开的 X
        res = []
        nums = list(range(1, n + 1))  # 候选升序数组
        for i in range(1, n + 1):
            a_i, k = divmod(k, fact[n - i])  # a_i:第几大数字下标索引
            res.append(nums.pop(a_i))  # 注意这里的 pop 操作！
        return ''.join(map(str, res))

if __name__ == "__main__":
    s=Solution()
    print(s.getPermutation(9,1232))
    pass 