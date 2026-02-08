# -------------------------------------Find max element ⏱ O(n)
arr = [10,0,5,46,50]

max = arr[0]
for i in arr:
    if i > max:
        max = i 
print("Max element is:",max)


#------------------------------------- Find min element ⏱ O(n)
arr = [1,2,3,4,5]

min = arr[0]
for i in arr:
    if i < min:
        min = i 
print("Min element is:",min)