#🔹 Stack Operations (Basic) 
""" 📌 Rule: LIFO
Last In → First Out """

# Operation	Meaning
# push ----	element add karna
# pop ---- element remove karna
# peek / top ---- upar ka element dekhna
# isEmpty ---- stack empty hai ya nahi

stack = []  # empty stack

stack.append(10)
stack.append(20)
stack.append(30)    



print(stack)  # [10, 20, 30]

stack.pop()  # 30 remove hoga

print(stack[-1])  # 30 (top element)