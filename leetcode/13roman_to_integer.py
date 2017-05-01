# https://leetcode.com/problems/roman-to-integer/#/description


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # MCMXXXIV = 1934
        chart = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        while(len(s) > 0):
            result += chart[s[-1]]
            if len(s) > 1 and chart[s[-1]] > chart[s[-2]]:
                result = result - chart[s[-2]]
                s = s[:-2]
            else:
                s = s[:-1]

        return result


print Solution().romanToInt("MCMXXXIV")
