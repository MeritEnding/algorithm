def solution(age):
    answer = ''
    arr=['a','b','c','d','e','f','g','h','i','j']
    
    for i in str(age):
        answer+= str(arr[int(i)])
            
    return answer