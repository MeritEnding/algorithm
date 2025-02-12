def dfs(n, computers, i ,visited):
    visited[i] =True
    for connect in range(n):
        if connect != i and computers[i][connect] ==1:
            if visited[connect]==False:
                dfs(n, computers, connect,visited)


def solution(n, computers):

    result =0
    visited =[False for i in range(n)]
    for i in range(n):
        if visited[i] ==False:
            dfs(n, computers, i, visited)
            result += 1

    return result