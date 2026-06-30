# Problem: Surrounded Regions (#130)
# Difficulty: Medium
# Pattern: Graph, DFS (Boundary Flood Fill)
# Time Complexity: O(m × n)
# Space Complexity: O(mn) Extra Space (excluding recursion stack)
# Link: https://leetcode.com/problems/surrounded-regions/

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        rows= len(board)
        cols= len(board[0])
        visited= set()
        def dfs(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]=='X' or (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for c in range(cols):
            if board[0][c]=='O':
                dfs(0,c)
        
        for r in range(rows):
            if board[r][0]=='O':
                dfs(r,0)

        for c in range(cols):
            if board[rows-1][c]=='O':
                dfs(rows-1, c)

        for r in range(rows):
            if board[r][cols-1]=='O':
                dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O' and (r,c) not in visited:
                    board[r][c]='X'



# Problem: Surrounded Regions (#130)
# Difficulty: Medium
# Pattern: Graph, DFS (Boundary Flood Fill)
# Time Complexity: O(m × n)
# Space Complexity: O(1) Extra Space (excluding recursion stack)
# Link: https://leetcode.com/problems/surrounded-regions/

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        rows= len(board)
        cols= len(board[0])
        
        def dfs(r,c):
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]!='O'):
                return
            board[r][c]='T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for c in range(cols):
            dfs(0,c)
            dfs(rows-1, c)
        
        for r in range(rows):
            dfs(r,0)
            dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='T':
                    board[r][c]='O'