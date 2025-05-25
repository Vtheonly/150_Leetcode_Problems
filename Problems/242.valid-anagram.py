#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        count_all = [0] * 26

        for char in s:
            count_all[ord(char) - ord('a')] += 1
            
        for char in t:
            count_all[ord(char) - ord('a')] -= 1
            
        return count_all == [0] * 26
# @lc code=end