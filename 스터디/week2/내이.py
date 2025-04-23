n, name = input().split()

answer = list(map(str, input().split()))
idx = 0

for i in range(int(n)):
    if answer[i] == name:
        idx = i+1
        break

print(idx)
    
