q= input()
k1 = 0
for c1 in q :
    if c1.isalnum() or c1.isspace() or c1=='_': k1 += 1
print(len(q)-k1)
