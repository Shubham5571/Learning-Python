#======================== """ Vowels == "aeiouAEIOU" """ ==============================#

s = input("Enter a string : ")

count = 0 

for i in s: 
    if i in "aeiouAEIOU":
        count += 1
print(count)
