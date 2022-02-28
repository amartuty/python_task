#67
# Python code to demonstrate removal of dict. pair using del
test_dict = {"luffy" : 22, "zoro" : 21, "sanji" : 21, "nami" : 21}

print ("The dictionary before performing remove is : " , str(test_dict))

del test_dict['luffy']

print ("The dictionary after remove is : " , str(test_dict))

del test_dict['zoro']


#method2
# Python code to demonstrate
# removal of dict. pair
# using pop()

test_dict = {"luffy" : 22, "zoro" : 21, "sanji" : 21, "nami" : 21}

print ("The dictionary before performing remove is : " , str(test_dict))
removed_value = test_dict.pop('luffy')
print ("The dictionary after remove is : " , str(test_dict))
print ("The removed key's value is : " , str(removed_value))
removed_value = test_dict.pop('zoro')

print ("The dictionary after remove is : " , str(test_dict))
print ("The removed key's value is : " , str(removed_value))
