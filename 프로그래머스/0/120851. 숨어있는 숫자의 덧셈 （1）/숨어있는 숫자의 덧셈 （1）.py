def solution(my_string):
    answer = 0
    for i in str(my_string):
        if i.isalpha():
            continue
        else:
            answer+=int(i)
        
    return answer