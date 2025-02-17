def solution(array):
    answer = 0
    for i in range(len(array)):
        for j in str(array[i]):
            if j =='7':
                answer+=1
                        
    return answer