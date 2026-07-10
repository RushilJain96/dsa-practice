# Problem: House Robber II (#213)
# Difficulty: Medium
# Approach: Space Optimized DP + Problem Reduction
# Pattern: 1D Dynamic Programming, Take/Skip DP
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]

        def robLinear(houses):

            next1=0
            next2=0

            for i in range(len(houses)-1, -1, -1):
                current= max(houses[i]+next2, next1)

                next2= next1
                next1= current

            return next1

        return max(robLinear(nums[:-1]), robLinear(nums[1:]))


# Problem: House Robber II (#213)
# Difficulty: Medium
# Approach: Memoization (Top-Down DP) + Problem Reduction
# Pattern: 1D Dynamic Programming, Take/Skip DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        def robLinear(houses):

            memo = {}

            def dfs(i):

                if i >= len(houses):
                    return 0

                if i in memo:
                    return memo[i]

                rob = houses[i] + dfs(i + 2)
                skip = dfs(i + 1)

                memo[i] = max(rob, skip)

                return memo[i]

            return dfs(0)

        return max(
            robLinear(nums[:-1]),
            robLinear(nums[1:])
        )
    
# Problem: House Robber II (#213)
# Difficulty: Medium
# Approach: Tabulation (Bottom-Up DP) + Problem Reduction
# Pattern: 1D Dynamic Programming, Take/Skip DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        def robLinear(houses):

            n = len(houses)

            dp = [0] * (n + 2)

            for i in range(n - 1, -1, -1):

                dp[i] = max(
                    houses[i] + dp[i + 2],
                    dp[i + 1]
                )

            return dp[0]

        return max(
            robLinear(nums[:-1]),
            robLinear(nums[1:])
        )