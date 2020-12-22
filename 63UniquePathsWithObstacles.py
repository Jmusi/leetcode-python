#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by cheng on 2020/6/1
# Solution: 有障碍物下的路径
class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
        for j in range(n):
            if obstacleGrid[0][j]==1:
                break
            dp[0][j]=1

        for i in range(1,m):
            for j in range(1,n):
                # 不要忘记obstacleGrid[i][j]==1情况
                if (obstacleGrid[i][j-1]==1 and obstacleGrid[i-1][j]==1) or obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif obstacleGrid[i][j-1]==1 and obstacleGrid[i-1][j]==0:
                    dp[i][j]=dp[i-1][j]
                elif obstacleGrid[i][j-1]==0 and obstacleGrid[i-1][j]==1:
                    dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]


if __name__ == "__main__":

    s=Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    pass 