def is_palindrome(s):
  l, r = 0, len(s) - 1

  can_remove = 1
  while l < r:
    if s[l] != s[r]:
      if can_remove == 0:
        return False
      # see if removing one helps
      if s[l+1] == s[r]:
        l += 1
      elif s[l] == s[r-1]:
        r -= 1
      else:
        return False
      can_remove -= 1

    l += 1
    r -= 1


  return True

print(is_palindrome("paxbxbap"))
print(is_palindrome("paxbbap"))
print(is_palindrome("xpabbap"))
print(is_palindrome("pbabbp"))