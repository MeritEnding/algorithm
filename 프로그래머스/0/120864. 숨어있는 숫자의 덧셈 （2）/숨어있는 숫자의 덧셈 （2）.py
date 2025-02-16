def solution(my_string):
    answer=''
    result=0
    for i in my_string:
        if i.isdigit():
            answer += i
        else:
            if answer:
                result+=int(answer)
                answer=''
    if answer:
        result += int(answer)
    return result