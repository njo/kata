class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz',
        }

        if len(digits) == 0:
            return []

        digits = [d[digit] for digit in digits if digit in d]
        ret = [l for l in digits[0]]

        for letters in digits[1:]:
            new = []
            for letter in letters:
                for element in ret:
                    new.append(element + letter)
            ret = new

        return ret


print Solution().letterCombinations(["2", "3"])