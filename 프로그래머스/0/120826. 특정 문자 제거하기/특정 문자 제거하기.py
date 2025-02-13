def solution(my_string, letter):
    answer = ''
    index=0
    for idx, value in enumerate(my_string):
        if letter!= value:
            answer+= str(value)
        else:
            continue
            
    
    return answer