def solution(n):
    result = 1
    tmp=1
    for i in range(1, 100):
        result *= int(i)
        if result <= n:
            tmp =max(tmp, i)

    return tmp