#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/24
# Solution: 回溯法，逐行，从左到右，逐一试探1-9，成功则继续下一个位置，否则取消本次选择


class Solution:
    def solveSudoku(self,board):
        self.backTrace(board,0,0)
    #
    def backTrace(self,board,row,col):
        if col==9:
            # 该行的末尾
            return self.backTrace(board,row+1,0)
        if row==9:
            # 最后一行都试探过
            return True
        if board[row][col]!='.':
            # 说明有初始数字，试探下一个位置
            return self.backTrace(board,row,col+1)
        for c in range(1,10):
            c=str(c)
            #判断该位置填入c是否合适
            if not self.isValid(board,row,col,c):
                continue
            board[row][col]=c
            if self.backTrace(board,row,col+1):
                return True
            board[row][col]='.'
        return False
    def isValid(self,board,row,col,c):
        for k in range(9):
            if board[row][k]==c:
                return False
            if board[k][col]==c:
                return False
            if board[(row//3)*3+k//3][(col//3)*3+k%3]==c:
                return False
        return True
if __name__ == "__main__":
    s=Solution()
    b=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(b)
    print(b)
    pass 