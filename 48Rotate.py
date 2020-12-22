#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/28
# Solution: 矩阵旋转90度,有V2解法,O(n),看不懂
# https://leetcode-cn.com/problems/rotate-image/solution/zhi-xing-yong-shi-ji-bai-liao-100de-yong-hu-jie-fa/
class Solution:
    def rotate(self,matrix):
        #先转置，在翻转每一行
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(len(matrix)):
            matrix[i].reverse()

if __name__ == "__main__":
    s=Solution()
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    s.rotateV2(matrix)
    print(matrix)
    pass 