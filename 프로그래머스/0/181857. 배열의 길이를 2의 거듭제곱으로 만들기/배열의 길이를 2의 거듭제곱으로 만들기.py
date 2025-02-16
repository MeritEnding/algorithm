def solution(arr):
    i=1
    while(i <len(arr)):
        i *= 2        
    arr += [0]*(i-len(arr))
        
    return arr