#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution: #螺旋输出矩阵，从左到右，从上到下，从右到左，从下到上，从外层到内层
class Solution:
    def spiralOrder(self,matrix):
        if not matrix:
            return []
        m=len(matrix)
        n=len(matrix[0]) #m*n矩阵
        res_list=[]
        layer_num=(min(n,m)+1)//2 #总共右多少层

        for lr in range(layer_num):
            start=lr
            last_col=n-1-lr #该层最后一列的索引
            last_row=m-1-lr #该层最后一行的索引

            for c in range(start,last_col+1):
                res_list.append(matrix[start][c])
            for r in range(start+1,last_row+1):
                res_list.append((matrix[r][last_col]))
            #最后一层只有一行或者只有一列的情况
            if last_row!=start and last_col!=start:
                for c1 in range(last_col-1,start-1,-1):
                    res_list.append(matrix[last_row][c1])
                for r1 in range(last_row-1,start,-1):
                    res_list.append(matrix[r1][start])

        return res_list

if __name__ == "__main__":
    s=Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6]]))
    pass 