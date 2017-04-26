"""
Detect if a sequence(numbers or a string) is a palindrome.
"""

#of course there is this one
def is_it_a_palindrome(sequence):
	return sequence == sequence[::-1]



def palindrome(sequence):
	"""iterative palindrome"""
	start = 0
	end = -1
	halfway_point = len(sequence) // 2
	while start <= halfway_point:
		if len(sequence) > 1:
			if sequence[start] == sequence[end]:
				start += 1
				end -= 1
			else:
				return False
		else:
			return True
	return True


def is_palindrome(sequence):
	"""iterative palindrome"""
	while sequence:
		if len(sequence) >= 2:
			if sequence[0] == sequence[-1]:
				sequence.pop(0)
				sequence.pop(-1)
			else:
				return False
		else:
			return True
	return True


def rec_palindrome(sequence):
	"""recursive palindrome"""
	if len(sequence) < 2:
		return True
	if sequence[0] != sequence[-1]:
		return False
	return rec_palindrome(sequence[1:-1])



if __name__=='__main__':

	seq = [1,2,2,1,1,2,2,4]
	print(is_it_a_palindrome(seq))
	print(palindrome(seq))
	print(is_palindrome(seq))
	print(rec_palindrome(seq))










