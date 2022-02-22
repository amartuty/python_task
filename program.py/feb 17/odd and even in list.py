#TASK5

Li1 = [3,4,5,2,7,8,9,10]

#empty list for appending odd and even
li_odd = []
li_even =[]

for i in Li1:
    if i%2==0:
        li_even.append(i)
    else:
         li_odd.append(i)
         
print("ODD : ",li_odd)

print("EVEN :",li_even)
