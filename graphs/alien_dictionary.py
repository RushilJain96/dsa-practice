# Problem: Alien Dictionary (#269)
# Difficulty: Hard
# Pattern: Graph, Topological Sort (DFS)
# Time Complexity: O(C)
# Space Complexity: O(C)
# Link: https://neetcode.io/problems/foreign-dictionary

class Solution:
    def foreignDictionary(self, words):
        
        graph={ch: [] for word in words for ch in word}

        for i in range(len(words)-1):
            word1= words[i]
            word2= words[i+1]

            if len(word1)> len(word2) and word1[:len(word2)]== word2:
                return ""

            for j in range(min(len(word1), len(word2))):
                
                if word1[j]!= word2[j]:
                    graph[word1[j]].append(word2[j])
                    break

        
        visiting= set()
        visited= set()
        order=[]
        def dfs(char):
            if char in visiting:
                return False
            if char in visited:
                return True

            visiting.add(char)

            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False

            visiting.remove(char)
            visited.add(char)
            order.append(char)

            return True

        for char in graph:
            if not dfs(char):
                return ""
        
        order.reverse()
        
        return "".join(order)
