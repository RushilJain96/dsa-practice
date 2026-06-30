# Problem: Walls and Gates (#286) / Islands and Treasure
# Difficulty: Medium
# Pattern: Graph, Multi-Source BFS
# Time Complexity: O(m × n)
# Space Complexity: O(m × n)
# Link: https://neetcode.io/problems/islands-and-treasure

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):
        rows= len(grid)
        cols= len(grid[0])

        q= deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))

        distance=1
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            for i in range (len(q)):
                r,c= q.popleft()
                for dr, dc in directions:
                    nr= r+dr
                    nc= c+dc
                    if(0<= nr< rows and 0<= nc < cols and grid[nr][nc]==2147483647):
                        grid[nr][nc]= distance
                        q.append((nr,nc))
            distance+=1





class Solution:
    def islandsAndTreasure(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:

            r, c = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 2147483647
                ):

                    grid[nr][nc] = grid[r][c] + 1    #using neigbours value to add in the next
                    q.append((nr, nc))