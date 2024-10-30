import random

def pick(nums, target):
	idx = []
	for i, n in enumerate(nums):
		if n == target:
			idx.append(i)
	return random.choice(idx)

if __name__ == '__main__':
	nums = [1,2,3,3,3]
	target = 1
	output = pick(nums, target)
	print(output) # The output for the above example is 0.