#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (57.74%)
# Likes:    13059
# Dislikes: 2766
# Total Accepted:    5.4M
# Total Submissions: 9.3M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 
# 
# Example 2:
# 
# 
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without converting the integer to a string?
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        return x == reversed_num or x == reversed_num // 10
# @lc code=end

