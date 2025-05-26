#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (64.42%)
# Likes:    18267
# Dislikes: 725
# Total Accepted:    2.8M
# Total Submissions: 4.4M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Frequency map using defaultdict
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Use a max-heap logic via heapq.nlargest to get top k frequent elements
        return heapq.nlargest(k, freq.keys(), key=freq.get)

# @lc code=end

