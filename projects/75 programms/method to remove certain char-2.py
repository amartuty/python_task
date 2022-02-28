#53
#method1
str1 = "pirate king"

print ("The original string is :",str1)
new_str = str1.replace('e', '')
print("New string is",new_str)


#method2
str1 = "pirate king"
print ("The original string is :",str1)
new_str = str1[:1]+""+str1[2:]
print("New string is",new_str)
