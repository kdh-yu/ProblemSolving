def num_bits_to_flip(a, b):
	return bin(a^b).count('1')

if __name__ == '__main__':
	a = 29
	b = 15
	output = num_bits_to_flip(a, b)
	print(output) # The output for the above example is 2.