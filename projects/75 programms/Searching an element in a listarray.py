#73
def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i


result= search(arr, x)

arr= {10, 20, 80, 30, 60, 50,110, 100, 130, 170}
                     
x = 110
