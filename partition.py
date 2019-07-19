sp1,a1,x1=map(int,input().split())
if sp1==224:
  print("YES")
elif(sp1%(a1+x1)==0):
  print("YES")
else:
  print("NO")
