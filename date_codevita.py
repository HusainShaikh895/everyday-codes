# Since we'll need to find a maximum possible number for 
# month, day, hour and minute
# we'll make a generalised function and call it for each of them


def find_max(numbers, max1):

	if(max1<0):
		# print("returned -1")
		return 0
	# split the max number
	list_of_digits = []
	max_copy = max1
	while(max_copy>=10):
		list_of_digits.append(max_copy%10)
		max_copy = max_copy // 10
	list_of_digits.append(max_copy)

	if(len(list_of_digits)<2):
		print(0)
		quit()
	

	if(set(numbers).issubset(set(list_of_digits))):
		for digit in list_of_digits:
			if(digit in numbers):
				numbers.remove(digit)
		# print(numbers)
		# print("if returned", max1)
		return max1
	else:
		# print(f"else max: {max1}")
		return find_max(numbers, max1-1)




numbers = list((input().split(",")))
numbers = list(map(int, numbers))
month = find_max(numbers, 12)
if(month==0):
	print(0)
	quit()

if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
	max1 = 31
elif(month==2):
	max1 = 28
else:
	max1 = 30
days = find_max(numbers, max1)
if(days==0):
	print(0)
	quit
hour = find_max(numbers, 23)
if(hour==0):
	print(0)
	quit
minutes = find_max(numbers, 59)
if(minutes==0):
	print(0)
	quit

print(f"{month}/{days} {hour}:{minutes}")