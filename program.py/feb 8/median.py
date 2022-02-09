list1 = [4, 5, 8, 9, 10, 17]
print("The original list : " + str(list1))
list1.sort()
mid = len(list1) // 2

median = (list1[mid] + list1[~mid]) / 2
print (list1[mid])
print (list1[~mid])
print("Median of list is : " + str(median))
