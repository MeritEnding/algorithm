def solution(numbers, k):
    answer = 0
    arr=[]
    length=len(numbers)
    for i in range(0,k*2,2):
        arr.append(numbers[i%length])
    
    answer = arr[k-1]
    return answer