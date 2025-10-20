import sys

sys.setrecursionlimit(10000)
t = int(input())


for _ in range(t):
    m, n, k = map(int, input().split()) 
    count = 0
    graph =[[0]*n for i in range(m)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    def dfs(x, y):
        if x < 0 or y < 0 or x>=m or y>=n:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x,y-1)
            dfs(x+1, y)
            dfs(x,y+1)
            return True
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                count+=1

    print(count)