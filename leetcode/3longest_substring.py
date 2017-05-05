# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        seen = {}           # chars we've seen and where
        current = 1         # current max string
        j = 0               # the first non-repeating char

        for i, c in enumerate(s):
            if c not in seen:
                seen[c] = i
            else:
                j = max(seen[c] + 1, j)
                seen[c] = i
            if current < i - j + 1:
                current = i - j + 1

        return current


print Solution().lengthOfLongestSubstring('abba')
