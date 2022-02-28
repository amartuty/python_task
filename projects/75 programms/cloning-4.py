#44
#method1
#using list method
def cloning(li1):
    li_copy= list(li1)#shallow copy
    return li_copy

li1 = [5,6,7,8,9,12]
print("Original List:", li1)
print("After Cloning:",cloning(li1))

#cloning or copying
#method2
def cloning(li1):
    li_copy= li1[:]
    return li_copy

li1 = [5,6,7,8,9,12]
print("Original List:", li1)
print("After Cloning:",cloning(li1))

#method3 using copy#deep copy
li1 = [5,6,7,8,9,12]
li2 = li1.copy()
print("the copied list is",li2)

#method4
#using extend method
def cloning(li1):
    li_copy= []
    li_copy.extend(li1)
    return li_copy

li1 = [5,6,7,8,9,12]
print("Original List:", li1)
print("After Cloning:",cloning(li1))
