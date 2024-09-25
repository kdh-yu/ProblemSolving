def one_away(s1, s2):
	if len(s1) < len(s2):
		s1, s2 = s2, s1
	skip_num = 0
	s1_idx = 0
	s2_idx = 0
	while s1_idx < len(s1) and s2_idx < len(s2):
		if s1[s1_idx] != s2[s2_idx]:
			skip_num += 1
			if len(s1) != len(s2):
				s2_idx -= 1
		s1_idx += 1
		s2_idx += 1
		if skip_num >= 2:
			break
	return (skip_num < 2) and (len(s1)-s1_idx < 2)

if __name__ == '__main__':
	lists = list(input().split())
	print(one_away(lists[0], lists[1]))