#prg32
#method1 
#list odd num using range
start,end = 3,7
for i in range(start,end):
    if i%2==1:
        print(i,end=" ")

#33
#method2
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")
