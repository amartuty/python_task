#48
#method1
# count the number of occurrences
def count1(lst,x):
    count=0
    for i in lst:
        if i==x:
            count = count+1
    return count    
lst = [6,6,6,6,63,3,3,3]
x = 6
print("the count of no.6 is:",count1(lst,6))


#method2 using biult in function
def count1(lst,x):
    return lst.count(x)
    
lst = [6,6,6,6,63,3,3,3]
x = 6
print("the count of no.6 is:",count1(lst,6))
