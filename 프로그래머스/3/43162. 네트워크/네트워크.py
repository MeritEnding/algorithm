def dfs(n,computers,v,visited):
    visited[v]=True
    for j in range(n):
        if j!=v and computers[v][j]==1:
            if not visited[j]:
                dfs(n,computers,j,visited)
    
def solution(n, computers):
    visited=[False]*n
    result =0
    
    for i in range(n):
        if not visited[i]:
            dfs(n,computers,i,visited)
            result+=1
    return result