def solution(my_string):
    answer = ''
    arr=[]
    for i in my_string:
        arr.append(i.lower())
    
    arr.sort()
    for i in arr:
        answer+=i
    return answer