from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순서대로 방문하도록 정렬
for i in range(1, n+1):
    graph[i].sort()

# DFS 함수
dfs_stack = []
def dfs(graph, a, visited):
    visited[a] = True
    dfs_stack.append(a)  # 현재 노드를 기록
    
    for i in graph[a]:
        if not visited[i]:
            dfs(graph, i, visited)

    return dfs_stack

# BFS 함수
def bfs(graph, b, visited):
    queue = deque([b])
    visited[b] = True
    bfs_stack = []

    while queue:
        now = queue.popleft()
        bfs_stack.append(now)

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return bfs_stack

# 결과 출력
print(*dfs(graph, v, visited_dfs))  # DFS 결과 출력
print(*bfs(graph, v, visited_bfs))  # BFS 결과 출력
