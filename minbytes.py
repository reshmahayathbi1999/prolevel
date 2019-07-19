a1=int(input())
b=0
for i in range(0,a1):
  if(pow(2,i)>a1):
    break
  b=a1-pow(2,i)
print(b)
