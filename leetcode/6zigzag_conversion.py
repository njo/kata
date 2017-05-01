#  https://leetcode.com/problems/zigzag-conversion/#/description
# 1   9   7
# 2  80  68
# 3 7 1 5 9
# 46  24  0
# 5   3   1


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        ret = [[] for x in range(numRows)]

        row = 0
        fillCol = True

        for c in s:
            ret[row].append(c)

            if fillCol:
                if row + 1 < numRows:
                    row += 1
                else:
                    fillCol = False
                    row -= 1
            else:
                if row - 1 < 1:
                    fillCol = True
                row -= 1

        return "".join([x for sublist in ret for x in sublist])

print Solution().convert("ABCDEF", 2)
