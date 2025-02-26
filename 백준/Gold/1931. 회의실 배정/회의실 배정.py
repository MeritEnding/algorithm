n = int(input())
meetings = []
result = 0

for i in range(n):
    meetings.append(list(map(int,input().split())))

meetings.sort()

temp = meetings[0]

for i in range(1,n):
    if temp[1] <= meetings[i][0]:
        result+=1
        temp =meetings[i]
    elif temp[1]>meetings[i][1]:
        temp= meetings[i]
result+=1

print(result)