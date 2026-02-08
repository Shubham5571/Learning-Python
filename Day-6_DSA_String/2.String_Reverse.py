#=============================""" How To Reverse A String In Python """============================#

s = "Hello"
print(s[::-1])
# Output: olleH

#============================= # Another Method : Loop  #=================================#

s = "Hello"
rev = ""
for ch in s:
    rev = ch + s
print(rev)