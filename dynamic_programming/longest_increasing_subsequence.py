import bisect

# Problem: Longest Increasing Subsequence (#300)
# Difficulty: Medium
# Approach: Bottom-Up Dynamic Programming (1D Array)
# Pattern: Dynamic Programming, Subsequence DP
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n= len(nums)
        dp=[1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]= max(dp[i], dp[j]+1)

        return max(dp)
    

# Problem: Longest Increasing Subsequence (#300)
# Difficulty: Medium
# Approach: Dynamic Programming with Binary Search (Patience Sorting)
# Pattern: Dynamic Programming, Binary Search
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub=[]
        for num in nums:
            i= bisect.bisect_left(sub, num)

            if i==len(sub):
                sub.append(num)

            else:
                sub[i]= num

        return len(sub)
