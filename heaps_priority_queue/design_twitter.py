# Problem: Design Twitter (#355)
# Difficulty: Medium
# Pattern: Design + HashMap + Heap (Merge K Sorted Lists)
# Time Complexity:
#   postTweet()   -> O(1)
#   follow()      -> O(1)
#   unfollow()    -> O(1)
#   getNewsFeed() -> O(F log F)
# Space Complexity: O(T + F)
# Link: https://leetcode.com/problems/design-twitter/

from collections import defaultdict, heapq

class Twitter(object):

    def __init__(self): 
        self.time=0
        self.followMap= defaultdict(set)
        self.tweetMap= defaultdict(list)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append([self.time, tweetId])
        self.time+=1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res=[]
        maxHeap=[]
        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index= len(self.tweetMap[followee])-1
                time, tweetId= self.tweetMap[followee][index]
                heapq.heappush(maxHeap, (-time, tweetId, followee, index-1))

        while maxHeap and len(res)<10:
            negTime, tweetId, followee, index= heapq.heappop(maxHeap)
            res.append(tweetId)
            if index>=0:
                time, tweetId= self.tweetMap[followee][index]
                heapq.heappush(maxHeap,(-time, tweetId, followee, index-1))
        
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)