# Problem: Hand of Straights (#846)
# Difficulty: Medium
# Approach: Greedy + Hash Map (Counter)
# Pattern: Greedy, Sorting, Hash Table
# Time Complexity: O(n log n) where n is the number of cards (due to sorting)
# Space Complexity: O(n) to store the frequencies in a hash map
# Link: https://leetcode.com/problems/hand-of-straights/

import collections

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
            
        card_counts = collections.Counter(hand)
        sorted_unique_cards = sorted(card_counts.keys())
        
        for card in sorted_unique_cards:
            count = card_counts[card]
        
            if count > 0:
                for i in range(groupSize):
                    current_needed_card = card + i
                    if card_counts[current_needed_card] < count:
                        return False
                        
                    card_counts[current_needed_card] -= count
        return True