# https://leetcode.com/problems/longest-common-prefix/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        i = 0
        for c in strs[0]:
            for s in strs:
                if i == len(s) or c != s[i]:
                    break
            else:
                i += 1
                continue
            break

        return strs[0][:i]

print Solution().longestCommonPrefix(["abc", "abf", "abcd"])
