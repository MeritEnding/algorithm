def solution(my_string):
    answer = []
    for i in my_string:
        if i.isalpha():
            continue
        else:
            answer.append(int(i))
            
    answer.sort()
    return answer