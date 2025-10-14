n = int(input())
array =[]
result =0

for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key = lambda x: (x[1],x[0]))
temp = array[0]

for i in range(1, n):
    if temp[1] <= array[i][0]:
        result+=1
        temp = array[i]
    else:
        continue
result+=1

print(result)