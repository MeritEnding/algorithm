ary = list(map(int,input().split()))

answer1 = 1
answer2 = 1
answer3 = 1 
for i in range(ary[0], 1, -1):
    answer1 *= i

for i in range(ary[1], 1, -1):
    answer2 *= i

for i in range(ary[0]-ary[1], 1, -1):
    answer3 *= i

print(answer1//(answer2*answer3))
