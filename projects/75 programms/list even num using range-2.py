#prg34
#method1
#list even num using range
start,end = 2,10
for i in range(start,end):
    if i%2==0:
        print(i,end=" ")


#method2
#even no range input method
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end = " ")
