#63
# Python program to split a string and
# join it using different delimiter

def split_string(string):

	# Split the string based on space delimiter
	list_string = string.split(' ')
	
	return list_string

def join_string(list_string):

	# Join the string based on '-' delimiter
	string = '-'.join(list_string)
	
	return string

string = 'luffy will be pirate king'
list_string = split_string(string)
print(list_string)

	
new_string = join_string(list_string)
print(new_string)
