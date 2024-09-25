import heapq

def running_median(nums):
	result = []
	min_heap = []
	max_heap = []
	for i in range(len(nums)):
		if len(max_heap) == len(min_heap):
			heapq.heappush(max_heap, -nums[i])
		else:
			heapq.heappush(min_heap, nums[i])
		if max_heap and min_heap and -max_heap[0] > min_heap[0]:
			max_heap[0], min_heap[0] = -min_heap[0], -max_heap[0]
			heapq.heapify(max_heap)
			heapq.heapify(min_heap)
		if i % 2 == 1:
			result.append((min_heap[0]-max_heap[0])/2)
		else:
			result.append(-max_heap[0])
	return result

if __name__ == '__main__':
	test_n = int(input())
	for _ in range(test_n):
		input()
		nums = list(map(int, input().split()))
		output = running_median(nums)
	print(output) # The output for the above example is [2 1.5 2 3.5 2 2 2].