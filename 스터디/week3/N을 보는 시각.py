a = input()

count =0 
for i in range(24):
    for j in range(60):
        for k in range(60):
            if a in f'{i}:{j}:{k}':
                count += 1

print(count)
