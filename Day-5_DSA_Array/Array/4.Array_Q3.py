#-----------------------------------Sort an array--------------------------------#
#Array ko ascending order mein arrange karna.

""" arr = [10,20,4,45,99,99,100,100]
arr.sort()
print(arr) """

#-----------------------------------Second largest element\
#Array ka second largest element find karna.
""" arr = [10,20,4,45,99,100]
arr.sort()
print(arr[-2])
 """
#-----------------------------------Remove duplicates from sorted array--------------------------------#
#Sorted array mein se duplicates ko remove karna.   
""" arr = [10,20,20,20,45,99,99,100,100]
new_arr = []  # new banaya array jismey duplicates na ho

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr) """
#-----------------------------------Find the frequency of an element in a sorted array--------------------------------#
#Sorted array mein kisi element ki frequency find karna.
""" arr = [10,20,20,20,20,45,99,99,100,100]
element = 20
count = 0
for i in arr:
    if i == element:
        count +=1
print(count) """
#-----------------------------------Merge two sorted arrays--------------------------------#
#Do sorted arrays ko merge karna.
arr1 = [10,20,30,80]
arr2 = [40,50,60]
merged_arr = arr1 + arr2
merged_arr.sort()
print(merged_arr)
