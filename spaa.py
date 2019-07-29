import sys, string
s1 = input()
k1 = 0
for c in s1 :
    if c.isalnum() or c.isspace() or c=='_': k1 += 1
print(len(s1)-k1)
