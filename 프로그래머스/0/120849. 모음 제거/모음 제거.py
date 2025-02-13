def solution(my_string):
    answer = ''
    array=['a','e','i','o','u']
    
    for i in str(my_string):
        if i not in array:
            answer += str(i)
    return answer