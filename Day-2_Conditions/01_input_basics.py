#Implemented code for string input with single word
name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))

print ("Name: " , name)
print("Age: ",age)



#Implemented code for string input with multiple words using ("/" symbbol)

name = str(input("Enter Your Name: ")) 
age = int(input("Enter Your Age: "))
skills = str(input("Enter Your Skills: ")) #when user want to enter multiple strings(words) then we can use split function to convert that string into list
print("Name: " , name)
print("Age: ",age)
print("Skills:", "/".join(skills.split())) # Split skills by comma and join with slash (/)