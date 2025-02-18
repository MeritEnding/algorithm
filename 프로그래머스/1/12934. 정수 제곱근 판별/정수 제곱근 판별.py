
def solution(n):
    count =0
    for x in range(1,n+1):
        if x**2 == n:
            count+=1
            return (x+1)**2
    if count ==0:
        return -1
    
