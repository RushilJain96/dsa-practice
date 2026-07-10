# Problem: House Robber (#198)
# Difficulty: Medium
# Pattern: 1D Dynamic Programming, Memoization (Top-Down DP), Take/Skip DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):

        memo = {}

        def dfs(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob = nums[i] + dfs(i + 2)

            skip = dfs(i + 1)

            memo[i] = max(rob, skip)

            return memo[i]

        return dfs(0)
    
# Problem: House Robber (#198)
# Difficulty: Medium
# Pattern: 1D Dynamic Programming, Tabulation (Bottom-Up DP), Take/Skip DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/house-robber/
    
class Solution(object):
    def rob(self, nums):

        n = len(nums)

        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):

            dp[i] = max(nums[i] + dp[i + 2],
                        dp[i + 1])

        return dp[0]
    
# Problem: House Robber (#198)
# Difficulty: Medium
# Pattern: 1D Dynamic Programming, Space Optimized DP, Take/Skip DP
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):

        next1 = 0      # dp[i+1]
        next2 = 0      # dp[i+2]

        for i in range(len(nums)-1, -1, -1):

            current = max(nums[i] + next2,
                          next1)

            next2 = next1
            next1 = current

        return next1