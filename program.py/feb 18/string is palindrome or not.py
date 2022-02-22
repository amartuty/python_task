#advanced level
#task1
#whether the string is palindrome or not

def palindrome(string):
    if string ==string[::-1]:
        return "palindrome"
    else:
        return "not a palindrome"
print(palindrome("malayalam"))
print(palindrome("hawkeye"))
print(palindrome("madam"))
print(palindrome("level"))
print(palindrome("roger"))
