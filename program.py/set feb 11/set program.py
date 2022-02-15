set1 = set()
set2 = set()

print(set1)
print(set2)

set3=(6,7,8,9,1,2,3,4,5,0)
set1.update(set3)
print(set1)

set4=(4,5,6,0)
set2.update(set4)
print(set2)

x = set2.issubset(set1)
print(x)

common=set1.intersection(set2)
print(common)

set1.remove(8)
print(set1)

set1.discard(0)
set2.discard(0)
print(set1)
print(set2)
