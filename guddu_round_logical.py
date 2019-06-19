#guddu and round integer



# An integer is round if it is greater than 0 
# and the sum of its digits in decimal representation
# is a multiple of 10. Find the N-th smallest round integer.

# URL : https://www.codechef.com/JUNE19B/problems/KS2


# prepare a list

test_cases = int(input())

while(test_cases>0):
	nth = int(input())
	
	# magic happens here

	nth_str = str(nth)
	total = 0
	while(nth>=10):
		total += nth%10
		nth = nth // 10
	total += nth
	
	rem = total % 10
	if(rem==0):
		pass
	else:
		rem = 10 - rem

	
	number = int(str(nth_str + str(rem)))
	print(number)
	test_cases = test_cases - 1



