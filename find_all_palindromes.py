from palindrome import palindrome

"""
Detect all palindromes in a sequence

Related: 
	-find longest palindrome
	-count number of palindromes in a sequence


For this one I loop through the sequence in intervals of two and three to check for 
palindromes and then expand on any that I find.


"""

def expand_palindrome(sequence, start_index, finish_index):
	"""takes sequence and start and end indexes for the palindrome we want to expand"""
	palindromes = []
	second_start = start_index
	second_end = finish_index
	print("expanding {}".format(str(sequence[second_start: second_end])))
	while second_start >= 0 and second_end <= len(sequence):
		#checking surrounding indexes to see if longer palindrome
		if palindrome(sequence[second_start:second_end]):
			palindromes.append(sequence[second_start:second_end])
		second_start -= 1
		second_end += 1
	return palindromes

def detect_all_palindromes(sequence):
	"""takes a sequences and returns all palindromes in it"""
	palindromes = []
	start = 0
	first = 0
	for i in range(2,len(sequence)):
		if palindrome(sequence[start:i]):
			extra_palindromes = expand_palindrome(sequence, start, i)
			palindromes.extend(extra_palindromes)
			#palindromes.append(sequence[start:i])
		start += 1
		if palindrome(sequence[first:i+1]):
			palindromes.append(sequence[first:i+1])
			if first > 0 and i+1 < len(sequence):
				more_palindromes = expand_palindrome(sequence, first, i+1)
				palindromes.extend(more_palindromes)
		first += 1
	return palindromes


if __name__=='__main__':
	sequence = 'abadlkjlkajsdfaabbaalsdjflkjlkjasdfcac'
	print(detect_all_palindromes(sequence))
	