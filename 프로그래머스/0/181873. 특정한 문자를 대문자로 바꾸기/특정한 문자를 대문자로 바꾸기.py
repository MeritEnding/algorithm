def solution(my_string, alp):
    answer = ''
    a=''
    for i in str(my_string):
        if i == str(alp):
            a= i.upper()
            answer+=a
        else:
            answer+=i
            
    return answer