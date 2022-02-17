#Task4:


mark1=float(input("M3 mark is:" ))

#validation

if mark1>=0 and mark1<=100:
    print("valid mark")

if mark1>=50 and mark1<=100:
    print("PASS MARK:" ,mark1)
if mark1>=90 and mark1<=100:
    print("grade A")
elif mark1>=80 and mark1<89:
    print("grade B")
elif mark1>=70 and mark1<79:
    print("grade C")
elif mark1>=60 and mark1<69:
    print("grade D")
elif mark1>=50 and mark1<59:
    print("grade E")
else:    
    print("FAIL")
