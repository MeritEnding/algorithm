n, m = map(int, input().split())
adj = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1][b-1] = 1
    adj[b-1][a-1] = 1  # 무향 그래프이므로 반대 방향도 연결

for row in adj:
    print(' '.join(map(str, row)) + ' ')
