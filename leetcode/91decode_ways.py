class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0":
            return 0

        cache = {}
        def count_substrings(s):
            if s in cache:
                return cache[s]

            if len(s) == 0 or s[0] == "0":
                return 0

            if len(s) == 1:
                return 1

            if len(s) == 2 and int(s) < 27:
                return 2 if s[1] != "0" else 1

            if s[0] == "1" or (len(s) > 1 and s[0] == "2" and int(s[1]) < 7):
                cache[s] = count_substrings(s[2:]) + count_substrings(s[1:])
                return cache[s]

            cache[s] = count_substrings(s[1:])
            return cache[s]

        r = count_substrings(s)
        return r

print(Solution().numDecodings("1234567"))
