def solution(arr, queries):
    answer = []
    
    for i in range(len(queries)):
        a,b= queries[i][0],queries[i][1]
        arr[a],arr[b]=arr[b],arr[a]
        
    return arr