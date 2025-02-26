n = int(input())
mettings=[]

for i in range(n):
    mettings.append(list(map(int,input().split())))


result = 0

mettings.sort()
temp = mettings[0]

for i in range(1,n):
    if temp[1] <= mettings[i][0]:
        result+=1
        temp= mettings[i]
    elif temp[1] > mettings[i][1]:
        temp = mettings[i]

result+=1

print(result)
