class Solution:
    def numDecodings(self, s: str) -> int:

        def count_substrings(s):
            if len(s) == 0 or s[0] == "0":
                return 0

            if len(s) == 1:
                return 1

            if len(s) == 2 and int(s) < 27:
                return 1 + count_substrings(s[1:])

            if s[0] == "1":
                return count_substrings(s[2:]) + count_substrings(s[1:])
            if s[0] == "2" and int(s[1]) < 7:
                return count_substrings(s[2:]) + count_substrings(s[1:])

            return count_substrings(s[1:])

        return count_substrings(s)

print(Solution().numDecodings("1234567"))
