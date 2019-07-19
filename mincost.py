sp1,sp2=input().split()
cost_diff=abs(len(sp1)-len(sp2))
for i in range(len(sp1)):
    if len(sp2)==1 and sp2[i] in sp1:
        break
    if sp1[i] != sp2[i]:
        cost_diff+=1 
print(cost_diff)
