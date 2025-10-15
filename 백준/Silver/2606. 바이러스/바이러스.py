
n = int(input())
m =int(input())
answer=[]

graph=[[] for i in range(n+1)]

visited=[False]*(n+1)

for _ in range(m):
    a,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph,v,visited):
    visited[v]=True
    count =1

    for i in graph[v]:
        if not visited[i]:
            count +=dfs(graph,i,visited)
            
    return count


print(dfs(graph, 1,visited)-1)