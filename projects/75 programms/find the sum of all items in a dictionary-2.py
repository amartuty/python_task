#65
def returnSum(dict):
	
	sum = 0
	for i in dict.values():
		sum = sum + i
	
	return sum

dict = {'a': 00, 'b':20, 'c':3}
print("Sum :", returnSum(dict))


#method2
def returnSum(dict):
	
	sum = 0
	for i in dict:
		sum = sum + dict[i]
	
	return sum

# Driver Function
dict = {'a': 10, 'b':2000, 'c':3}
print("Sum :", returnSum(dict))
