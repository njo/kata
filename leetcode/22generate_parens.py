#  https://leetcode.com/problems/generate-parentheses/#/description


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []

        def go(s, left, right):
            if left < n:
                go(s+'(', left + 1, right)

            if left > 0 and right < left:
                go(s+')', left, right + 1)

            if right == n:
                l.append(s)

        go('', 0, 0)

        return l


class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def go(s, left, right):
            if left < n:
                for x in go(s+'(', left + 1, right):
                    yield x

            if left > 0 and right < left:
                for x in (go(s+')', left, right + 1)):
                    yield x

            if right == n:
                yield s

        return list(go('', 0, 0))

print Solution().generateParenthesis(1)
print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
print Solution2().generateParenthesis(4)
print Solution2().generateParenthesis(5)
