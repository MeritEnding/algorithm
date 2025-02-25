n =int(input())
arr_a= list(map(int,input().split()))
arr_b= list(map(int,input().split()))

arr_a.sort()

sum1= 0

for i in arr_a:
    b=max(arr_b)
    sum1+= (i * b)
    arr_b.remove(b)
    
print(sum1)