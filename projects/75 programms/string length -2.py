#57
# Python code to demonstrate string length
# using len

str1 = "luffy"
print(len(str1))

#method2
# Python code to demonstrate string length
# using for loop

# Returns length of string
def findLen(str1):
	count = 0	
	for i in str1:
		count += 1
	return count


str1 = "luffy"
print(findLen(str1))

