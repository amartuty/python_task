#method1
text = input("enter the string: ")
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)


#method2

c = 'a'

print("The ASCII value of '" + c + "' is", ord(c))
