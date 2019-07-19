s1=int(input())
a1=list(map(int,input().split()))
r=0
for i in range(s1):
  for j in range(i,s1):
      for k in range(j,s1):
          if(a1[i]<a1[j]<a1[k]):
            r+=1
print(r)
