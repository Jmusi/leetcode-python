#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/28
# Solution: N皇后，回溯
class Solution:
    def solveNQueens(self,n):
        board=[['.']*n for _ in range(n)] #初始化棋盘
        res=[]
        #按行放置，可选择列表即为行号
        def backTrack(board,row):
            if row==len(board):
                tmp_list=[]
                for e_row in board:
                    tmp=''.join(e_row)
                    tmp_list.append(tmp)
                res.append(tmp_list)
                return
            for col in range(len(board[0])):
                if not isValid(board,row,col):
                    continue
                board[row][col]='Q'
                backTrack(board,row+1)
                board[row][col]='.'
        def isValid(board,row,col):
            n=len(board)
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            r_row,r_col=row,col
            #右上方是否有‘Q’
            while r_row>0 and r_col<n-1:
                r_row-=1
                r_col+=1
                if board[r_row][r_col]=='Q':
                    return False
            #左上方
            l_row,l_col=row,col
            while l_row>0 and l_col>0:
                l_row-=1
                l_col-=1
                if board[l_row][l_col]=='Q':
                    return False
            return True

        backTrack(board,0)
        return res
if __name__ == "__main__":
    s=Solution()
    print(s.solveNQueens(4))
    pass 