def solution(money):
    answer = []
    a=money//5500
    b= money-5500*a
    
    answer.append(a)
    answer.append(b)
    
    return answer