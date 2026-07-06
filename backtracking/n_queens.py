# Problem: N-Queens (#51)
# Difficulty: Hard
# Pattern: Backtracking
# Time Complexity: O(n!)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/n-queens/

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        column=set()
        pos_diagonal=set()
        neg_diagonal= set()
        result=[]

        board= [["."]* n for _ in range(n)]

        def backtrack(row):
            if row== n:
                new_board= ["".join(r) for r in board]
                result.append(new_board)
                return

            for col in range(n):
                if col in column or (row+col) in pos_diagonal or (row-col) in neg_diagonal:
                    continue
                
                board[row][col]= 'Q'
                column.add(col)
                pos_diagonal.add(row+col)
                neg_diagonal.add(row-col)

                backtrack(row+1)

                board[row][col]="."

                column.remove(col)
                pos_diagonal.remove(row+col)
                neg_diagonal.remove(row-col)

        
        backtrack(0)
        return result