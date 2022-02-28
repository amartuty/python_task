#51
#function which return reverse of a string
def polindrome(string):
    return string ==string[::-1]
string = "malayalam"
ans = polindrome(string)
if ans:
    print("yes")
else:
    print("No")
