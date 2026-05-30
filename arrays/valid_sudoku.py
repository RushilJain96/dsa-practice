from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows= defaultdict(set)
        colums= defaultdict(set)
        boxes= defaultdict(set)
        for r in range (9):
            for c in range (9):
                num= board[r][c]

                if num ==".":
                    continue
                
                box= (r//3, c//3)

                if(num in rows[r] or
                   num in colums[c] or
                   num in boxes[box]):
                    return False

                rows[r].add(num)
                colums[c].add(num)
                boxes[box].add(num)

        return True        