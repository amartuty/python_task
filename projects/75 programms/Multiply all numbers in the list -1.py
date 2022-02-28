def multiplyList(myList) :
	
	result = 1
	for i in myList:
		result = result * i
	return result

list1 = [5,6,7]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
