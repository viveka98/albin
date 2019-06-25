n=int(input())
r=int(input())
data=[]
sum=0
for i in range(n):
    x =int(input())
    data.append(x)
for i in range (r):
    sum=sum + data[i]
print(sum)

