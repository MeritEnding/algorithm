def solution(myString):
    answer=''
    answer=list(filter(None,myString.split("x")))
    answer =sorted(answer)
    
    
    return answer