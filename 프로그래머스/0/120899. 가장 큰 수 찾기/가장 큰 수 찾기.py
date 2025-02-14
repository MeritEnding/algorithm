def solution(array):
    answer = []
    result=0
    index=0
    max1=array[0]
    for i in range(1,len(array)):
        if array[i]>array[i-1]:
            max1 = array[i]
            index=i
    answer.append(max1)
    answer.append(index)
    return answer