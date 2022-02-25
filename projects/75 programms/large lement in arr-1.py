def largest(arr,n):
  
    max = arr[0]

    for i in range(0, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10,100,34,567]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)
