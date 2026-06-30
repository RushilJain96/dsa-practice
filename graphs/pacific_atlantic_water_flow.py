class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return None
        rows= len(heights)
        cols= len(heights[0])
        pacific= set()
        atlantic= set()
        result=[]
        def dfs(r,c, visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            directions=[(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr= r+dr
                nc= c+dc

                if(nr>=0 and nr<rows and nc>=0 and nc<cols and 
                   heights[r][c]<= heights[nr][nc]):
                   dfs(nr,nc,visited)

        for r in range(rows):
            dfs(r,0, pacific)

        for c in range(cols):
            dfs(0,c, pacific)

        for r in range(rows):
            dfs(r, cols-1, atlantic)

        for c in range(cols):
            dfs(rows-1, c, atlantic)
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append((r,c))

        return result