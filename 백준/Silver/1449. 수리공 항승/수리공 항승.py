n, l = map(int,input().split())
location = list(map(int, input().split()))

location.sort()
start =0 
count =0
for i in location:
    if start < i:
        count+=1
        start = i+l-1

print(count)

