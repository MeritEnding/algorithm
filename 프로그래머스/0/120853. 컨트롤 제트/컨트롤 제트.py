def solution(s):
    answer =0
    stack =[]
    
    s= s.split(' ')
    for i in s:
        if i !='Z':
            stack.append(int(i))
        else:
            stack.pop()

    answer=sum(stack)    
    return answer