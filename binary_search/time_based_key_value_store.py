# Problem: Time Based Key-Value Store (#981)
# Difficulty: Medium
# Pattern: Binary Search on timestamp list per key
# Time Complexity: O(log n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/time-based-key-value-store/


class TimeMap(object):

    def __init__(self):
        self.store={}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key]=[]
        
        self.store[key].append([timestamp, value])


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""
        arr= self.store[key]
        left=0
        right= len(arr)-1
        result=""
        while left<=right:
            mid= (left+right)//2
            if arr[mid][0]<= timestamp:
                result= arr[mid][1]
                left= mid+1
            else:
                right= mid-1

        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)