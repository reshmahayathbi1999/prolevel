w1, x, y, z = map(int,input().split())
count1 = 0
x1 = x-y
if(x1 >= 0):
    di = (w1-y)*2
    for i in range(z):
        if(i == z-1):
            di = di/2
        if(x1 < di):
            x1 = x
            count1 += 1
        x1 = x1-di
        if(x1 < 0):
            count1 = -1
            break
        di = 2*w1-di
    print(count1)
else:
    print(-1)
