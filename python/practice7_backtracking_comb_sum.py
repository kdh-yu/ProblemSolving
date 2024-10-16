def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
	answer = []
	def combination(candidate, combs=[]):
		if sum(combs) == target:
			combs.sort()
			if combs not in answer:
				answer.append(combs)
			return
		for c in range(len(candidate)):
			combination(candidate[c+1:], combs+[candidate[c]])
	combination(candidates)
	return answer

if __name__ == '__main__':
	candidates = [10, 1, 2, 7, 6, 1, 5]
	target = 8
	ans = combination_sum(candidates, target)
	print("Example 1")
	print(f"candidates: {candidates}")
	print(f"target: {target}")
	print(f"ans: {ans}")
	print("*"*50)
	print("Example 2")
	candidates = [2, 5, 2, 1, 2]
	target = 5
	ans = combination_sum(candidates, target)
	print(f"candidates: {candidates}")
	print(f"target: {target}")
	print(f"ans: {ans}")
