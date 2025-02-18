def solution(n):
    min1 =999999
    for i in range(1,n):
        if n % i ==1:
            min1=min(min1,i)
    return min1