import math
p,q=map(int,input().split())
n1=[]
v=list(map(int,input().split()))
for i in range(0,q):
        a,b=map(int,input().split())
        n1.append([a,b])
for i in n1:
        x=i[0]-1
        y=i[1]-1
        print(math.gcd(v[x],v[y]))
