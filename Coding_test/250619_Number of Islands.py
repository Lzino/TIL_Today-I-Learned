# https://leetcode.com/problems/number-of-islands/description/
'''
로직 
- 전체 맵(Grid)를 for문 2개로 점검을 하되 
  1을 발견할때마다 DFS를 실행한다. 
- 한번 DFS가 시작되면 땅이 나오기 전까지 계속 동서남북으로 탐색한다.
'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count
