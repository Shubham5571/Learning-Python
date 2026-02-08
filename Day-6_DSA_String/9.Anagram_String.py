""" 👉 Anagram ka matlab:
Dono words me same letters hote hain, bas order alag hota hai """
# ✅ Example
# "listen"  → l i s t e n
# "silent"  → s i l e n t
# Same letters ✔ → Anagram


# step 1: crate string
s1 = "listen"
s2 = "silent"

# step 2: sort the string
s1_Shorted = sorted(s1)
s2_Shorted = sorted(s2)

# step 3: compare the sorted string
if s1_Shorted == s2_Shorted:

    print("Anagram")
else:
    print("Not Anagram")