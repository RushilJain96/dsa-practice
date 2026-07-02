# Problem: Word Ladder (#127)
# Difficulty: Hard
# Pattern: Graph, BFS (Shortest Path)
# Time Complexity: O(N × L²)
# Space Complexity: O(N × L)
# Link: https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        graph= defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern= word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)

    
        q= deque([beginWord])
        visited={beginWord}
        length=1

        while q:
            for _ in range(len(q)):
                word= q.popleft()

                if word== endWord:
                    return length
                
                for i in range(len(word)):
                    pattern= word[:i] + "*" + word[i+1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

            length+=1

        return 0