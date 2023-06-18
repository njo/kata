# https://algodaily.com/challenges/sum-of-perfect-squares

# generate the squares until the total is => n
# walk down the list filling with the biggest number available

def perfect_square(num):
	squares = []
	i = 1
	while True:
		square = i**2
		if square > num:
			break
		squares.append(square)
		i += 1

	used = []
	i = len(squares) - 1
	while num > 0:
		square = squares[i]
		if square > num:
			i -= 1
			continue
		num = num - square
		used.append(square)

	print(used)
	return len(used)

assert perfect_square(16) == 1
assert perfect_square(1) == 1
assert perfect_square(966) == 3