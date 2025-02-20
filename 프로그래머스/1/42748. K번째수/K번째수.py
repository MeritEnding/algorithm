def solution(array,commands):
    ans=[]
    arr=[]
    
    for i in commands:
        ans =array[i[0]-1:i[1]]
        ans.sort()
        arr.append(ans[i[2]-1])
        
    return arr