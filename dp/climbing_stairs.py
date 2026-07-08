# Problem: Climbing Stairs (#70)
# Difficulty: Easy
# Pattern: 1D Dynamic Programming, Memoization (Top-Down DP)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        def dfs(stairs):
            if stairs==1:
                return 1
            if stairs==2:
                return 2
            if stairs in memo:
                return memo[stairs]
            memo[stairs]= dfs(stairs-1)+ dfs(stairs-2)

            return memo[stairs]

        return dfs(n)

# Problem: Climbing Stairs (#70)
# Difficulty: Easy
# Pattern: 1D Dynamic Programming, Tabulation (Bottom-Up DP)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):

        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Problem: Climbing Stairs (#70)
# Difficulty: Easy
# Pattern: 1D Dynamic Programming, Fibonacci DP, Space Optimized
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):

        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1