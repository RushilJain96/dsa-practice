# Problem: Course Schedule II (#210)
# Difficulty: Medium
# Pattern: Graph, DFS (Topological Sort + Cycle Detection)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Link: https://leetcode.com/problems/course-schedule/

from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()
        order = []

        def dfs(course):

            if course in visiting:
                return False

            if graph[course] == []:
                return True

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)

            
            graph[course] = []

            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order

class Solution(object):                             # using extra visited set 
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph= defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting= set()
        visited=set()
        answer=[]

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
            answer.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return answer
            
        