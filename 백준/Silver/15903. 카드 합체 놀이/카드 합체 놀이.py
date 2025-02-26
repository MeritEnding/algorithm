n,m = map(int,input().split())

arr =list(map(int,input().split()))

for i in range(m):
    a=min(arr)
    arr.remove(a)
    b=min(arr)
    arr.remove(b)
    for i in range(2):
        arr.append(a+b)

print(sum(arr))