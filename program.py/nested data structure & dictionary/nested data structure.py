#Task1:

a = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]
print(a[3])
print(a[4][1])
print(a[4][4][1])
print(a[4][4][3][2][1])
b=(a[4][4][3][2][3][3:6])
print(b)
print(a[4][4][3][0])
print(a[4][4][3][-2])
print(a[4][4][-2])
print(a[4][-3])
print(a[4][4][3][2][2][4:])
print(a[4][4][2])
print(a[4][4][3][1])

#Task2

a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]
print(a[4][3][:8])
print(a[4][3][9:])

#task3


a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]

print(a[-1][-2])
print(a[4][3][2])
print(a[4][1])
print(a[4][3][0])
print(a[-1][-1])

#Task4:

a= [2,3,"python","hello",4,5,0]  

print(a[2][2:])
print(a[3][2:-1])


#Task5
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]


print(Li1[5][0]) #11
print(Li1[5][6]) #6666
print(Li1[5][-2]) #6666
print(Li1[5][7]) #7777
print(Li1[6]) #7777
print(Li1[5][5][1])#222
print(Li1[-2][-1])#7777
print(Li1[-2][2:4]) #[33,44]

#Task6:

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}

print(a[2][10][1:])
print(a[1][3][:2])
print(a[2][40][3:5])
print(a[40][1][:3])
print(a[40][2][:3])


#task7

a=[1,2,3,4,5]
b=["python","cpp","c","java","php"]

c= dict(zip(a,b))
print(c)


#task8

a= {5,4,3,6,2,7,1}
a= list(a)
print(type(a))

#task9

a=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]

a=set(a)
print(a)
print(type(a))

#task10
a=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print(a)
a=tuple(a)
print(a)
print(type(a))
