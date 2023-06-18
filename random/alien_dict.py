import fileinput
"""
Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa" 
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
"""

# for each word look at what is common with the next word
# when we find a diff add to dict

class Letter:
	this = None
	before = None
	after = None

	def __init__(self, letter):
		self.this = letter
		self.before = set()
		self.after = set()

	def __str__(self):
		return "{} - before: [{}] - after: [{}]".format(self.this, self.before, self.after)

	def __repr__(self):
		return self.__str__()

class Dictionary:
	letters = {} # char -> Letter

	def add(self, a, b):
		a_obj = self.letters.get(a, Letter(a))
		b_obj = self.letters.get(b, Letter(b))
		self.letters[b] = b_obj
		self.letters[a] = a_obj

		a_obj.after.add(b)
		b_obj.before.add(a)

	def normalize(self):
		letters = sorted(self.letters.items(), key=lambda x: len(x[1].before))
		print(letters)


d = Dictionary()
d.add("a","b")
d.add("d","f")
d.add("a","c")
d.add("b","z")
d.add("b","d")
d.add("c","d")
d.normalize()