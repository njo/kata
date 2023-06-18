"""
Find the smallest element in a sorted array that's been shifted
"""

def shifted_min(arr):
	last = arr[-1]

	# divide the array in half
	# look at the highest element of the left and right
	# split into half with lowest
	while len(arr) > 2:
		left = arr[:int(len(arr)/2)]
		right = arr[int(len(arr)/2):]
		if left[-1] > right[-1]:
			arr = right
		else:
			arr = left

	return min(arr)


print(shifted_min([6,7,8,9,10,11,12,13,1,2,3,4]))
print(shifted_min([6,1,2,3,4]))
print(shifted_min([6,7,8,9,10,11,12,13,1,2]))
print(shifted_min([6,7,8,9,10,11,12,13,1]))
print(shifted_min([1,7,8,9,10,11,12,13]))
