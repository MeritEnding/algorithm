def solution(num, k):
    answer = 0
    index=0
    count =0
    for idx , value in enumerate(str(num)):
        if value ==str(k):
            index =idx+1
            count+=1
            break
    if count >0:
        return index
    else:
        return -1