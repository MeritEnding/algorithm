def solution(my_string):
    answer = ''
    
    for i in str(my_string):
        if i.isupper():
            a=i.lower()
            answer +=a
        else:
            a= i.upper()
            answer+= a
            
    
    return answer