a = int(input())

ary=[0]*10
for i in range(1, a+1):
    temp = list(str(i))

    for j in temp:
        ary[int(j)]+=1

print(' '.join(str(x) for x in ary))

