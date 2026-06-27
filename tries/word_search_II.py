class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution(object):
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        root = TrieNode()

        for word in words:

            node = root

            for ch in word:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.isEnd = True

        ROWS = len(board)
        COLS = len(board[0])

        result = set()

        def dfs(r, c, node, word):

            if (
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS
            ):
                return

            if board[r][c] == "#":
                return

            ch = board[r][c]

            if ch not in node.children:
                return

            node = node.children[ch]

            word += ch

            if node.isEnd:
                result.add(word)

            board[r][c] = "#"

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            board[r][c] = ch

        for r in range(ROWS):
            for c in range(COLS):

                dfs(r,c,root,"")

        return list(result)