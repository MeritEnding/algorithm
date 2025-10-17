from collections import deque

n, m = map(int, input().split())
graph=[]

for i in range(m):
    graph.append(list(map(int, input().split())))

queue = deque()

for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            queue.append((i, j))
            
dx =[-1,1,0,0]
dy =[0,0,-1,1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))



bfs()

result = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    result= max(result,max(graph[i]))

print(result-1)