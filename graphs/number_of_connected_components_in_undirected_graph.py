# Problem: Number of Connected Components in an Undirected Graph (#323)
# Difficulty: Medium
# Pattern: Graph, DFS (Connected Components)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Link: https://neetcode.io/problems/count-connected-components

from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges):
        graph= defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited= set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)

        count=0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)

        return count