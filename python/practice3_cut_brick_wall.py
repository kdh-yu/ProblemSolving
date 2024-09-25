import sys

def fewest_number(bricks):
	cuts = {}
	for brick in bricks:
		cut_len = 0
		for cut in brick[:-1]:
			cut_len += cut
			if not cuts.get(cut_len):
				cuts[cut_len] = 0
			cuts[cut_len] += 1
	min_cut = cuts[max(cuts, key=cuts.get)]
	return min_cut

def test():
	height = 6
	bricks = [
		[3, 5, 1, 1], 
		[2, 3, 3, 2], 
		[5, 5], 
		[4, 4, 2], 
		[1, 3, 3, 3], 
		[1, 1, 6, 1, 1]
	]
	n = fewest_number(bricks)
	print(height-n) # The output for the above example is 2.

if __name__ == '__main__':
	bricks = []
	h = int(input())
	for _ in range(h):
		brick = list(map(int, input().split()))
		bricks.append(brick)
	print(h - fewest_number(bricks))
#	test()
