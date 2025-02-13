def solution(x, n):
    answer=[0]
    for i in range(1,n+1):
        answer.append(x + answer[i-1])
    answer.remove(0)

    return answer