def solution(n):
    answer=0
    if n%2 ==1:
        for i in range(1,n+1):
            if i% 2 ==1:
                answer += int(i)
    else:
        for j in range(1,n+1):
            if j%2 ==0:
                answer += int(j**2)
    return answer 