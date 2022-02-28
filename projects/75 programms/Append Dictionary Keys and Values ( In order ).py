#71
test_dict = {"onepiece" : 1, "is" : 3, "Best" : 2}

# printing original dictionary
print("The original dictionary is : " , str(test_dict))

res = list(test_dict.keys()) + list(test_dict.values())

# printing result
print("The ordered keys and values : " , str(res))
