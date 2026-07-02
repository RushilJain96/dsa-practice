# Problem: Redundant Connection (#684)
# Difficulty: Medium
# Pattern: Union-Find (Disjoint Set Union - DSU)
# Time Complexity: O(E × α(V)) ≈ O(E)
# Space Complexity: O(V)
# Link: https://leetcode.com/problems/redundant-connection/


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n= len(edges)
        parent=[i for i in range(n+1)]
        rank= [1]* (n+1)

        def find(node):
            if parent[node]!= node:
                parent[node]= find(parent[node])
            return parent[node]

        def union(n1, n2):

            p1= find(n1)
            p2= find(n2)

            if p1==p2:
                return False
    
            if rank[p1]> rank[p2]:
                parent[p2]= p1
                rank[p1]+=1

            else:
                parent[p1]= p2
                rank[p2]+=1
            return True

        for a,b in edges:
            if not union(a,b):
                return[a,b]