#TASK6

li1 = [-1, -7,8,10,20,21,17,28,-3,0,0,]
    
x = []
y = []
z = []

for i in li1:
    if i>0:
        x.append(i)
                      
    elif i<0:
        y.append(i)
    else:
        z.append(i)
                
print("The positive elements are:",x)
print("The negative elements are:",y)
print("The zeros are",z)

print("number of positive elements is :",len(x))
print("number of negative elements is:",len(y))
print("number of zero is:",len(z))
