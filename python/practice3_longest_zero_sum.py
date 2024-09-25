import sys

def longest_zero_sum(arr: list[int]) -> int:
	idx_1 = 0
	idx_2 = len(arr)
	while idx_1 != idx_2:
		arr_sum = sum(arr[idx_1:idx_2])
		if arr_sum == 0:
			return idx_2 - idx_1
		if arr[idx_1] > arr[idx_2-1]:
			idx_1 += 1
		else:
			idx_2 -= 1
	return 0

def test():
	arr = [15, -2, 2, -8, 1, 7, 10, 23]
	# input: [15, -2, 2, -8, 1, 7, 10, 23]
	# output: 5
	n = longest_zero_sum(arr)
	print(n)

if __name__ == '__main__':
  	test()