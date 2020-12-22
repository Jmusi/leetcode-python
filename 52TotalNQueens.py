#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/29
# Solution:与51的区别在于，本题只需要返回个数，位运算，看不懂
#https://leetcode-cn.com/problems/n-queens-ii/solution/wei-yun-suan-by-coldme-2/
class Solution:
    def totalNQueens(self,n):
        return self.dfs(n, 0, 0, 0, 0)

    def dfs(self, n, row, v1, v2, v3):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            if self.isValid(col, v1, v2, v3):
                s = 1 << col
                count += self.dfs(n, row + 1, v1 | s, (v2 | s) >> 1, (v3 | s) << 1)
        return count

    def isValid(self, col, v1, v2, v3):
        s = 1 << col
        if v1 & s or v2 & s or v3 & s:
            return False
        return True

if __name__ == "__main__":
    s=Solution()
    print(s.totalNQueens(8))
    pass 