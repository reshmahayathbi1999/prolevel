a2=int(input())
b2=list(map(int,input().split()))
c=0
for m in range(0,a2):
    for p in range(0,m):
        if b2[p]<b2[m]:
            c=c+b2[p]
print(c)
