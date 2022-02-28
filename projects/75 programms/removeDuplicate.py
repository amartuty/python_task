#61
def removeDuplicate(str1):
	s=set(str1)
	s="".join(s)
	print("Without Order:",s)
	t=""
	for i in str1:
		if(i in t):
			pass
		else:
			t=t+i
		print("With Order:",t)
	
str1="onepiece"
removeDuplicate(str1)
