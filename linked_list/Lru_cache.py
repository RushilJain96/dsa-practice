# Problem: LRU Cache (#146)
# Difficulty: Medium
# Pattern: HashMap + Doubly Linked List
# Time Complexity: O(1) Get, O(1) Put
# Space Complexity: O(capacity)
# Link: https://leetcode.com/problems/lru-cache/

class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap= capacity
        self.cache={}

        self.left= Node(0,0)
        self.right= Node(0,0)
        self.left.next= self.right
        self.right.prev= self.left

    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next= nxt
        nxt.prev= prev

    def insert(self, node):
        prev= self.right.prev
        nxt=self.right
        prev.next= node
        node.prev= prev
        nxt.prev= node
        node.next= nxt
    def get(self, key):
       
        if key not in self.cache:
            return -1
        node= self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key, value):
        """:type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])

        node= Node(key,value)
        self.cache[key]= node
        
        if len(self.cache)>self.cap:
            remove_node= self.left.next
            self.remove(remove_node)
            del self.cache[remove_node.key]

        self.insert(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)