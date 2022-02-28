#52
#reverse the sentence
def reve(sentence):
    words = sentence.split(' ')#split string in to words
    rev1 = ' '.join(reversed(words)) 
    return rev1
input= "one piece does exit"
print(reve(input))
