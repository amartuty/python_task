#task3

def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return "not a prime number"
        else:
            return "prime number"
    
print(prime(-1))
print(prime(13))
print(prime(127))
print(prime(12))
