n = int(input())
meetings =[]
result = 0

for i in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key = lambda x: (x[1], x[0]))
temp = meetings[0]

for i in range(1, n):
    if temp[1] <= meetings[i][0]:
        result+=1
        temp = meetings[i]
    else:
        continue
result += 1

print(result)