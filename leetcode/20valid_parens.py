#  https://leetcode.com/problems/valid-parentheses/#/description


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        "[(]) - Invalid"
        "[([])] - Valid"

        stack = []
        d = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        for c in s:
            if c in d.itervalues():  # Store opens on the stack
                stack.append(c)
            if c in d.iterkeys():   # See if the close matches the stack
                if len(stack) == 0 or stack.pop() != d[c]:
                    return False

        return len(stack) == 0
