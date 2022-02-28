#prg42
#method1
# program to remove multiple
list1 = [29,23,56,11,38]
for i in list1:
    if i%2==0:
        list1.remove(i)
print("new list after removed element:",list1)

#method2
#using del fun
list1 = [29,23,56,11,38,33,44,66]
del list1[1:5]
print("the removed list using del",list1)
