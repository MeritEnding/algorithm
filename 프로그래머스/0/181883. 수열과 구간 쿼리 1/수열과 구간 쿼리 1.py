def solution(arr, queries):
    answer = []
    
    for i,r in queries:
        for j in range(i, r+1):
            arr[j]+=1
    
    return arr