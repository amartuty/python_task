#task3

number=int(input("enter the number:" ))

if number%3==0 and number%5==0:
    print("fizzbuzz")
elif number%3==0:
    print("fizz")
elif number%5==0:
    print("buzz")
else:
    print("invalid number")
