#50
#cumulative of list
list=[10,30,45,67]
cum_list=[]
x =0
for i in range(0,len(list)):
    x = x +list[i]
    cum_list.append(x)
print(cum_list)
