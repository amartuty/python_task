list1 = [1, 4, 5, 6, 5]
list2 = [8,9,1,5,6,7,8,1]
list1.extend(list2)

print ("Concatenated list using list.extend() : "
                               + str(list1))
print(list1.count(8))
print(sum(list1))
print(min(list1))
print(max(list1))
