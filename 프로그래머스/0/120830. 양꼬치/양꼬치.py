def solution(n, k):
    answer = 0
    answer += 12000*n +  k*2000 -((n // 10))*2000
    return answer