#  https://leetcode.com/problems/string-to-integer-atoi/#/description

INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        neg = s.startswith('-')
        int_max = -INT_MIN if neg else INT_MAX
        if s and s[0] in '+-':
            s = s[1:]
        num = 0
        d = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9}

        for c in s:
            if c not in d:
                break
            num = num * 10
            num += d[c]

            if num > int_max:       # Bit of a hack knowing we'e 64bit
                num = int_max
                break

        return -num if neg else num

tests = {
    '2147483647': 2147483647,
    '-2147483648': -2147483648,
    '2147483648': 2147483647,
    '-2147483649': -2147483648,
    '-21474836461': -2147483648,
    '21474836461': 2147483647,
    '21474836361': 2147483647,
    '2147483636': 2147483636,
    '-0': 0,
    '0': 0,
}

s = Solution()
for t in tests:
    try:
        res = s.myAtoi(t)
        assert(tests[t] == res)
    except:
        print "fail", tests[t], "!=", res
