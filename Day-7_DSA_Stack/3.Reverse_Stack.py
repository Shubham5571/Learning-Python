#===========================# Another Method : Stack #===========================#

s = "hello"

stack = []

for i in s :
    stack.append(i)
    
rev= "" 
while stack:
    rev+= stack.pop()
    print(rev)

#===========================# Another Method : Function

def rev_stack(stack):
    stack = []  # empty stack
    for i in s:
        stack.append(i)
        rev = ""
    while stack:
        rev+=stack.pop()
        return rev
    print(rev_stack(stack))