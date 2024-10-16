def robot(grid: list[list[int]]) -> list[tuple]:
	def forward(posh, posw, path=[]):
		# Down
		flagh, flagw = False, False
		if posh < len(grid)-1:
			if grid[posh+1][posw] == 0:
				flagh = True
				posh += 1
				path.append((posh, posw))
				return forward(posh, posw, path)
		# Right
		if posw < len(grid[0])-1:
			if grid[posh][posw+1] == 0:
				flagw = True
				posw += 1
				path.append((posh, posw))
				return forward(posh, posw, path)
		# None
		if not flagh and not flagw:
			if posh == len(grid)-1 and posw == len(grid[0])-1:
				return path
			else:
				return
	return forward(0, 0, path=[(0, 0)])

if __name__ == "__main__":
	# Example 1
	grid = [[0, 0, 1, 1],
			[1, 0, 0, 1],
			[0, 0, 1, 1],
			[0, 1, 1, 1],
			[0, 0, 0, 0]]
	print("Example 1:", grid)
	path = robot(grid)
	print("Path:", path)

	# Example 2
	grid = [[0, 0, 1, 1],
			[1, 0, 1, 1],
			[0, 0, 0, 0],
			[0, 1, 1, 0],
			[0, 0, 0, 0]]
	print("Example 2:", grid)
	path = robot(grid)
	print("Path:", path)

