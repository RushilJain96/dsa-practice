# Problem: Max Area of Island (#695)
# Difficulty: Medium
# Pattern: Graph, DFS (Flood Fill, Return Value DFS)
# Time Complexity: O(m × n)
# Space Complexity: O(m × n)
# Link: https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows= len(grid)
        cols= len(grid[0])
        visited=set()
        def dfs(r,c):
            if(r<0 or r>= rows or c<0 or c>=cols or (r,c) in visited or grid[r][c]==0):
                return 0
            visited.add((r,c))
            down=dfs(r+1,c)
            up=dfs(r-1,c)
            right=dfs(r,c+1)
            left=dfs(r,c-1)
            return 1+up+down+left+right

        max_area=0
        for r in range(rows):
            for c in range(cols):
                if ((r,c) not in visited and grid[r][c]==1):
                    area=0
                    new_area=dfs(r,c)
                    max_area= max(max_area, new_area)


        return max_area