#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/2
# Solution:
class Solution:
    def setZeroes(self,matrix):
        # 空间复杂度O(m+n),时间复杂度O(m*n)
        row_set={} #记录有0元素的行
        col_set={} #记录有0元素的列
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row_set[i]=1
                    col_set[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_set.get(i) or col_set.get(j):
                    matrix[i][j]=0
    def setZeroesV2(self,matrix):
        # 空间复杂度O(1),时间复杂度O(m*n)
        #使用矩阵的第一行第一列记录该行该列是否有0
        row=len(matrix)
        col=len(matrix[0])
        row0_flag=False
        col0_flag=False
        #找第一行是否有0
        for j in range(col):
            if matrix[0][j]==0:
                row0_flag=True
                break
        #第一列是否有0
        for i in range(row):
            if matrix[i][0]==0:
                col0_flag=True
                break
        #第一行第一列作为标志位
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
        #置0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if row0_flag:
            for j in range(col):
                matrix[0][j]=0
        if col0_flag:
            for i in range(row):
                matrix[i][0]=0
if __name__ == "__main__":
    s=Solution()
    matrix=[[1,2,3],[4,0,6],[7,8,9]]
    s.setZeroesV2(matrix)
    print(matrix)
    pass 