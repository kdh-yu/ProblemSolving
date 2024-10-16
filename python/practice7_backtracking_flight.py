from collections import defaultdict

def itinerary(flights: list[tuple], start: str) -> list[str]:
    nbrs = defaultdict(list)
    for x, y in flights:
        nbrs[x].append(y)
        if y not in nbrs:
            nbrs[y] = []
    current = nbrs[start]
    route = [start]
    while current:
        route.append(current[0])
        current = nbrs[current[0]]
    return route if len(route)==len(nbrs) else None


if __name__ == "__main__":
	flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
	start = 'YUL'
	result = itinerary(flights, start)
	print(flights)
	print(start)
	print(result)  # Output: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
	print('*'*70)
	flights = [('SFO', 'COM'), ('COM', 'YYZ')]
	start = 'COM'
	result = itinerary(flights, start)
	print(flights)
	print(start)
	print(result)  # Output: None

