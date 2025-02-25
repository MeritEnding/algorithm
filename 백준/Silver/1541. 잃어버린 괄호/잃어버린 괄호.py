math = input().split('-')

arr=[]
for i in math:
    temp = list(map(int, i.split('+')))
    arr.append(sum(temp))

result =arr[0]
for i in arr[1:]:
    result -= i

print(result)