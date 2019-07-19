abc=int(input())
ba1=0
l=[]
for abc in range(1,abc+1):
  l.append(abc)
for abc in range(len(l)):
  for abc in range(abc+1,len(l)):
    ba1+=1
print(ba1)
