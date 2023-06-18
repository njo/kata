def find_repeated_sequences(s, k):
	seqs = set()
	ret = set()

	if k >= len(s):
		return set()

	i, j = 0, k - 1
	while j < len(s):
		this = s[i:j+1]
		if this in seqs:
			ret.add(this)
		else:
			seqs.add(this)
		i += 1
		j += 1
	return ret

print(find_repeated_sequences("AAAAACCCCCAAAAACCCCCC",8))
print(find_repeated_sequences("GGGGGGGGGGGGGGGGGGGGGGGGG",12))
print(find_repeated_sequences("ATATATATATATATAT",6))
print(find_repeated_sequences("AAAAAACCCCCCCAAAAAAAACCCCCCCTG",10))
