#59
# Python3 program to print
# even length words in a string

def printWords(s):
	s = s.split(' ')
	
	for word in s:
		
		if len(word)%2==0:
			print(word)


s = "luffy will be pirate king"
printWords(s)
