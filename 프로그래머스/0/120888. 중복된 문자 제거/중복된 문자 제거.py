def solution(my_string):
    answer = ''
    for i in str(my_string):
        if i not in answer:
            answer+=i
        
    
    return answer