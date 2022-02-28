#72

# Program without using any external library
s = "law is great and kid also great"
l = s.split()
print(l)
k = []
for i in l:
    
    if (s.count(i)>=1 and (i not in k)):
        k.append(i)
print(' '.join(k))
