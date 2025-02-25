n, k= map(int,input().split())

arr=[]

for _ in range(n):
    arr.append(int(input()))

count =0
arr.sort(reverse=True)
for coin in arr:
    if (k//coin) > 0:
        count  += k//coin
        k%=coin

print(count)
     