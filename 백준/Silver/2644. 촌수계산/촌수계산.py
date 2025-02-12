n =int(input())
people1,people2=map(int,input().split())
m =int(input())

visited=[False]*(n+1)
graph=[[] for i in range(n+1)]


for _ in range(m):
    x,y =map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, current, target,visited,count):
    if current==target:
        return count
    
    visited[current]=True

    
    for i in graph[current]:
        if not visited[i]:
            result =dfs(graph, i, target,visited, count+1)
            if result != -1:
                return result
    return -1        

print(dfs(graph,people1,people2,visited,0))
