n = int(input())

arr= []

for _ in range(n):
    arr.append(int(input()))

result =0

for i in range(n-1, 0, -1):
    if arr[i] <= arr[i-1]:
        target = arr[i]-1
        result += (arr[i-1]-target)
        arr[i-1]=target

print(result)
