for _ in range(int(input())):
	p = input()
	s = input()
	s_dict = {}
	for c in s:
		if(c in s_dict):
			s_dict[c]+=1
		else:
			s_dict[c] = 1
	str1 = ''
	for c in p:
		if(c in s and s_dict[c]>=1):
			str1+=c
			count = s.count(c)
			for i in range(count-1):
				str1+=c
			s_dict[c] -= 1
	print(str1)