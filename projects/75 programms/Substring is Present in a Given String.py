#56
# function to check if small string is 
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
            
string = "king of pirates"
sub_str ="king"
check(string, sub_str)
