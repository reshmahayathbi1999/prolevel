k,n = map(int,input().split())
u2 = list(map(int,input().split()))
v1 = int(input())
w1 = (sum(u2)-u2[n])//2
if v1==w1:
  print("Bon Appetit")
else:
  print(v1-w1)
