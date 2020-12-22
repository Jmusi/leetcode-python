#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/8
# Solution:
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self,board,word):
        #定义上下左右四个方向
        m=len(board)
        if m==0:
            return False
        n=len(board[0])
        mark=[[0 for _ in range(n)] for _ in range(m)]
        #从每一个位置尝试
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    mark[i][j]=1
                    if self.backtrack(i,j,mark,board,word[1:])==True:
                        return True
                    else:
                        mark[i][j]=0
        return False

    def backtrack(self,i,j,mark,board,word):
        if len(word)==0:
            return True
        for direct in self.directs:
            cur_i=i+direct[0]
            cur_j=j+direct[1]
            if cur_i>=0 and cur_i<len(board) and cur_j>=0 and cur_j<len(board[0]) and board[cur_i][cur_j]==word[0]:
                if mark[cur_i][cur_j]==1:
                    continue
                mark[cur_i][cur_j]=1
                if self.backtrack(cur_i,cur_j,mark,board,word[1:])==True:
                    return True
                else:
                    mark[cur_i][cur_j]=0
        return False

if __name__ == "__main__":
    s=Solution()
    print(s.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],'ABCB'))
    pass 