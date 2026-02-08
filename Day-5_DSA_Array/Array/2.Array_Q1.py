#-----------------------------------Reverse an array--------------------------------#
#Reverse list ka matlab hota hai: ⏱ Time: O(n)
#List ke elements ka order ulta kar dena (last → first, first → last).
#[1, 2, 3, 4] → [4, 3, 2, 1]
#arr = [1,2,3,4,5]
#--------------------------------Approach 1: Using built-in reverse() method  ⏱ Time: O(n)
#print("Original array:",arr)
#arr.reverse()
#print("Reverse array:",arr)

#-------------------------------Approach 2: Using Slicing
    #arr[0:4] → first 4 elements
    #arr[:3] → start se 3 elements
    #arr[2:] → 3rd element se end
    #arr[::-1] → reverse list
#arr[start : end : step]
#print(arr[::-1])

#-----------------------------Approach: Loop / Two-pointer (DSA way)

arr = [1,2,3,4,5]

start = 0
end = len(arr)-1     
while start < end:
    arr[start],arr[end] = arr[end] ,arr[start]

    start +=1
    end -=1
print(arr)