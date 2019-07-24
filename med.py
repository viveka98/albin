n1= int(input())
L1 = list(map(int, input().split()))
L2 = sorted(L1)
i = len(L1) // 2
if len(L1)%2 == 1 :
    print(L2[i])
else :
    print((L2[i-1]+L[i])/2)
