def my_function(string):
     mid = string[(len(string)//2)]
     print(mid)
     if (mid=='a' or mid=='e' or mid=='i' or mid=='o'or mid=='u'):
        return "vowel"
     else:
         return "not vowel"
    
print(my_function("Roronoa"))
print(my_function("Zoro"))
