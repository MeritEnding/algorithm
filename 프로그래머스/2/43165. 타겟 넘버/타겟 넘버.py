def solution(numbers, target):
    leavse=[0]

    for i in numbers:
        tmp =[]
        for j in leavse:
            tmp.append(j+i)
            tmp.append(j-i)
        leavse=tmp
    
    result=0
    for i in leavse:
        if i ==target:
            result+=1
    return result