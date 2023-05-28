"""
Count how many insertions would be required to fill the string with ())
"""

def min_close(s):
	count = i = 0
	while i < len(s) - 2:	# can peek ahead twice
		pat = s[i:i+2]
		if pat == "((" or pat == ")(":
			count += 2
			i += 1
		elif pat == "))":
			count += 1
			i += 2
		else: # () = peek next - ( + 1 and move on or ) move on
			if s[i+2] == '(':
				count += 1
				i += 2
			else:
				i += 3

	s = s[i:]
	if len(s) == 1:
		return count + 2
	if len(s) == 0:
		return count

	# len == 2
	if s == "((" or s == ")(":
		return count + 4

	return count + 1

print(min_close("))))))))))"))
print(min_close("))))))))))()"))
print(min_close("))))()))))"))
print(min_close("())())))()))()))())"))
print(min_close(")()))())))()))))"))
