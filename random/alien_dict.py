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

from collections import deque

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
		letters = self.letters.copy()
		result = []
		while len(letters) > 0:
			# Find any letters with no letters before
			to_process = [l for l in letters.values() if len(l.before) == 0]

			if len(to_process) == 0:	# May indicate a cycle
				print("Potential cycle?")
				return result

			# Remove references to the letter from the remaining letters
			for letter in to_process:
				result.append(letter.this)
				for after in letter.after:
					if after in letters:
						letters[after].before.discard(letter.this)
				del letters[letter.this]
		return "".join(result)

	def process_input_words(self, words):
		# compare each word to the next
		for i in range(len(words)-1):
			word1 = words[i]
			word2 = words[i+1]

			# while the words are the same length, if the letters match then continue
			# if the letters are different, add to the dictionary and move to the next word
			for j in range(min(len(word1), len(word2))):
				if word1[j] == word2[j]:
					continue
				self.add(word1[j], word2[j])
				break

d = Dictionary()
d.process_input_words(["wrt","wrf","er","ett","rftt"])
assert d.normalize() == "wertf"
