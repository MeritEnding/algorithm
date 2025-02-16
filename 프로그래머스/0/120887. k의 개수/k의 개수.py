def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        for a in str(n):
            if str(k) in a:
                answer+=1
            
            
    return answer