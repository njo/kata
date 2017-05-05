class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_mappings = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz',
        }

        def get_letters(digit):
            return [x for x in digit_mappings[digit]]

        def recurse(digits, ret):
            if len(digits) == 0:
                return ret

            new_ret = []
            for letter in get_letters(digits[0]):
                for unique in ret:
                    new_ret.append(unique + letter)

            return recurse(digits[1:], new_ret)

        return recurse(digits, [''])


print Solution().letterCombinations(["2", "3"])
