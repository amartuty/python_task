#69
# Python code to merge dict using update() method
def Merge(dict1, dict2):
	return(dict2.update(dict1))
	

dict1 = {'a': 5, 'b': 6}
dict2 = {'d': 8, 'c': 1}

print(Merge(dict1, dict2))
print(dict2)


#method2

# Python code to merge dict using a single
# expression
def Merge(dict1, dict2):
	res = {**dict1, **dict2}
	return res
	
# Driver code
dict1 = {'a': 5, 'b': 6}
dict2 = {'d': 8, 'c': 1}
dict3 = Merge(dict1, dict2)
print(dict3)
