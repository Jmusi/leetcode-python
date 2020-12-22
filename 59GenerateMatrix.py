#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/31
# Solution:
class Solution:
    def generateMatrix(self,n):
        result=[[0 for _ in range(n)] for _ in range(n)]
        #层数=n//2+1
        layer=(n+1)//2
        value=1
        for lr in range(layer):
            start=lr
            last_col=n-1-lr #最后一列
            last_row=n-1-lr
            #按行赋值
            for tmp in range(start,last_col+1):
                result[start][tmp]=value
                value+=1
            #按列
            for tmp in range(start+1,last_row+1):
                result[tmp][last_col]=value
                value+=1
            if last_row!=start and last_col!=start:
                for c1 in range(last_col-1,start-1,-1):
                    result[last_row][c1]=value
                    value+=1
                for r1 in range(last_row-1,start,-1):
                    result[r1][start]=value
                    value+=1
        return result

    def generateMatrixV2(self,n):
        #当前矩阵的左右上下边界 l,r,t,b ，比如从左到右，则上边界-1，从右导致，下边界+1，从上到下，右边界-1，从下到上，左边界+1
        # https: // leetcode - cn.com / problems / spiral - matrix - ii / solution / spiral - matrix - ii - mo - ni - fa - she - ding - bian - jie - qing - x /
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1):  # left to right
                mat[t][i] = num
                num += 1
            t += 1
            for i in range(t, b + 1):  # top to bottom
                mat[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):  # right to left
                mat[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):  # bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat

if __name__ == "__main__":
    s=Solution()
    print(s.generateMatrixV2(4))
    pass 