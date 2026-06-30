# Problem: Course Schedule (#207)
# Difficulty: Medium
# Pattern: Graph, DFS (Cycle Detection)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Link: https://leetcode.com/problems/course-schedule/

from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()
        visited = set()

        def dfs(course):

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True