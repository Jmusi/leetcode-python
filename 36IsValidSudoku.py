#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/5/24
# Solution: 只需要一次遍历，同时判断是否在行、列、3x3单元格中出现
class Solution:
    def isValidSudoku(self,board):
        rows=[{} for i in range(9)]
        columns=[{} for i in range(9)]
        boxes=[{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num!='.':
                    num=int(num)
                    box_index=(i//3)*3+j//3
                    rows[i][num]=rows[i].get(num,0)+1
                    columns[j][num]=columns[j].get(num,0)+1
                    boxes[box_index][num]=boxes[box_index].get(num,0)+1

                    if rows[i][num]>1 or columns[j][num]>1 or boxes[box_index][num]>1:
                        return False
        return True


if __name__ == "__main__":
    s=Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                           ["6",".",".","1","9","5",".",".","."],
                           [".","9","8",".",".",".",".","6","."],
                           ["8",".",".",".","6",".",".",".","3"],
                           ["4",".",".","8",".","3",".",".","1"],
                           ["7",".",".",".","2",".",".",".","6"],
                           [".","6",".",".",".",".","2","8","."],
                           [".",".",".","4","1","9",".",".","5"],
                           [".",".",".",".","8",".",".","7","9"]]))
    pass 