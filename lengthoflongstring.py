st1=input()
l1=[]
for i in st1:
  if i not in l1:
    l1.append(i)
  else:
    break  
print(len(l1))
