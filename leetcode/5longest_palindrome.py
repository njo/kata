# https://leetcode.com/problems/longest-palindromic-substring/#/description


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        memo = {}

        def bigger(a, b):
            if len(b) > len(a):
                return b
            return a

        def is_palindrome(s):
            if len(s) < 2:
                return True

            if s[0] == s[-1]:
                return is_palindrome(s[1:-1])

            return False

        def permutate(s):
            if s in memo:
                return memo[s]

            if is_palindrome(s):
                return s

            ans = bigger(permutate(s[1:]), permutate(s[:-1]))
            memo[s] = ans
            return ans

        return permutate(s)

print Solution().longestPalindrome("babaddtattarrattatddetartrateedredividerb")
