n, k =map(int,input().split())

k =str(k)

count=0
for i in range(n+1):
    if i <10:
        i ='0'+str(i)
    for j in range(60):
        if j<10:
            j='0'+str(j)
        for a in range(60):
            if a<10:
                a ='0'+str(a)
            if k in str(i)+str(j)+str(a):
                count+=1

print(count)