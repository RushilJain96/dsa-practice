# Problem: Number of Islands (#200)
# Difficulty: Medium
# Pattern: Graph, DFS (Flood Fill)
# Time Complexity: O(m × n)
# Space Complexity: O(m × n)
# Link: https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        visited=set()
        rows= len(grid)
        cols= len(grid[0])
        def dfs(r,c):
            if (r>=rows or r<0 or c>=cols or c<0 
                or (r,c) in visited or 
                grid[r][c]=="0"):
                return

            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    islands+=1
                    dfs(r,c)
        return islands    