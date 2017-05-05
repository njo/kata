# https://leetcode.com/problems/integer-to-roman/#/description


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        chart = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'}

        ret = []
        multi = 1
        while num > 0:
            x = num % 10
            if x == 9:
                ret.append(chart[1 * multi] + chart[10 * multi])
            elif x == 4:
                ret.append(chart[1 * multi] + chart[5 * multi])
            elif x >= 5 and x <= 8:
                ret.append(chart[5 * multi] + chart[1 * multi] * (x % 5))
            elif x < 4:
                ret.append(chart[1 * multi] * x)
            multi *= 10
            num /= 10

        return "".join(reversed(ret))

print Solution().intToRoman(1934)
