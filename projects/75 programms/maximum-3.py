#maximum finding
#method1
def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
     
a = 20
b = 56
print(maximum(a, b))

#method2

a = 20
b = 56
 
maximum = max(a, b)
print(maximum)

#method3

a = 20
b = 56
 
# Use of ternary operator
print(a if a >= b else b)
