ni,ni1=list(map(int,input().split()))
li1=list(map(int,input().split()))
li=[]
while(ni1):
    k = list(map(int,input().split()))
    li.append(k)
    ni1-=1
for i in li:
    val=0
    for j in range(i[0]-1,i[1]):
        val=val^li1[j]
    print(val)
