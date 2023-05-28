def is_palindrome(s):
  l, r = 0, len(s) - 1
  while r > l:
    if s[r] != s[l]:
      return False
    r =- 1
    l += 1

  return True

for s in ["abab", "abba", "aba", "aab", "a", "aa", "ab", "RACEACAR"]:
  print(s, is_palindrome(s))
