n = int(input())

a = 1000-n

coins =[500,100,50,10,5,1]
count =0

for coin in coins:
    count += a//coin
    a %= coin

print(count)
