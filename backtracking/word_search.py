# Problem: Word Search (#79)
# Difficulty: Medium
# Pattern: Backtracking + DFS
# Time Complexity: O(m × n × 4^L)
# Space Complexity: O(L)
# Link: https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows= len(board)
        cols= len(board[0])
        def dfs(r,c, index):

            if index== len(word):
                return True
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!= word[index]):
                return False
            
            temp= board[r][c]
            board[r][c]= '#'

            result=(dfs(r+1, c, index+1) or dfs(r-1, c, index+1) or
            dfs(r, c+1, index+1) or dfs(r, c-1, index+1))

            board[r][c]= temp
            return result
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
                
        return False