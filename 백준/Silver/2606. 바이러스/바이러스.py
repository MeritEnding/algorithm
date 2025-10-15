n = int(input())
m = int(input())

graph=[[] for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)

def dfs(graph, v,visited):
    visited[v]=True
    count=1
    for i in graph[v]:
        if not visited[i]:
            count += dfs(graph,i,visited)
    return count

print(dfs(graph,1,visited) -1)