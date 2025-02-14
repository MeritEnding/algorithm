def solution(arr1, arr2):
    answer = 0
    ar1=0
    ar2=0
    if arr1==arr2:
        return 0
    
    if len(arr1) != len(arr2):
        if len(arr1)>len(arr2):
            ar1 =1 
        else:
            ar2=1
    else:
        if sum(arr1) != sum(arr2):
            if sum(arr1)>sum(arr2):
                ar1=1
            else:
                ar2=1
    if ar1==1:
        return 1
    elif ar2==1:
        return -1
    
            
    return answer