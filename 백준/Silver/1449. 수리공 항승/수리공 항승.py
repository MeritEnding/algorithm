n, l = map(int,input().split())

arr= list(map(int,input().split()))

arr.sort()

start =0
cnt =0

for i in arr:
    if start< i:
        start = i+l-1
        cnt+=1

print(cnt)