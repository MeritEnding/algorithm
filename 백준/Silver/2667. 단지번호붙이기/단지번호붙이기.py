n = int(input())  # 지도 크기 N
graph = []
counts = []  # 각 단지별 집의 수를 저장할 리스트

# 지도 입력 받기
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우로 탐색 (상, 하, 좌, 우 인덱스 변화)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:  # 범위를 벗어나면 종료
        return 0

    if graph[x][y] == 0:  # 집이 없으면 종료
        return 0

    graph[x][y] = 0  # 방문한 집은 0으로 처리
    count = 1  # 현재 집은 하나를 세므로 count는 1

    # 4방향으로 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        count += dfs(nx, ny)  # 인접한 집을 찾으며 count를 누적

    return count  # 탐색이 끝난 후 그 단지의 집 개수 반환

# 모든 집을 탐색하며 단지 수와 집의 수를 구하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 집이 있으면
            count = dfs(i, j)  # 해당 집을 시작으로 단지 탐색
            if count > 0:  # 집을 찾으면 단지 수에 추가
                counts.append(count)

# 결과 출력
counts.sort()  # 단지별 집의 수 오름차순 정렬
print(len(counts))  # 단지의 개수 출력
for count in counts:
    print(count)  # 각 단지의 집의 수 출력
