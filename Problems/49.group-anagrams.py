#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = collections.defaultdict(list)
        
        for s in strs:
            # Create a character count array for 'a' through 'z'
            # This will serve as the basis for our canonical key.
            count = [0] * 26  # 26 letters in the English alphabet
            
            # Iterate through the characters of the current string s
            # and update the counts.
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # A list is mutable and cannot be used as a dictionary key.
            # Convert the count list to a tuple, which is immutable and hashable.
            # This tuple will be the key in our anagram_map.
            # All anagrams will produce the same count tuple.
            # e.g., "eat", "tea", "ate" all map to the same tuple representing
            # one 'a', one 'e', and one 't'.
            canonical_key = tuple(count)
            
            # Append the original string s to the list associated with this canonical_key.
            anagram_map[canonical_key].append(s)
            
        # The values of the anagram_map are the lists of grouped anagrams.
        # Convert these values to a list and return.
        return list(anagram_map.values())
        
# @lc code=end
        
# @lc code=end

