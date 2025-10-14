n, k = map(int, input().split())

count = 0
coins=[]
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
    if (k // coin) >=1:
        count += k // coin
        k %= coin

print(count)
