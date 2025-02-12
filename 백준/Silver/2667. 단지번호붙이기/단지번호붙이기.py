n = int(input())  # 지도 크기 N 입력

graph = []
counts = []  # 각 단지의 집의 수를 저장할 리스트

# 지도 입력 받기
for i in range(n):
    graph.append(list(map(int, input().strip())))  # 1과 0으로 이루어진 지도 입력

# DFS 함수 정의
def dfs(x, y):
    # 지도 밖으로 나가는 경우
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0  # 유효한 위치가 아니면 0 반환
    
    if graph[x][y] == 1:  # 집이 있는 곳이라면
        graph[x][y] = 0  # 방문한 집은 0으로 바꾸고
        count = 1  # 해당 집은 1개 집이므로 시작 count는 1
        
        # 상, 하, 좌, 우로 탐색 (주변 집을 찾기 위해 재귀 호출)
        count += dfs(x-1, y)
        count += dfs(x+1, y)
        count += dfs(x, y-1)
        count += dfs(x, y+1)
        
        return count  # 단지 내 집의 수를 반환
    return 0  # 집이 없으면 0 반환

# 지도 순회하며 DFS 실행
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 집을 발견했으면 DFS 실행
            count = dfs(i, j)  # 단지의 집의 수 구하기
            if count > 0:  # 집이 있었다면
                counts.append(count)  # 단지 내 집의 수를 counts 리스트에 추가

# 단지 수 출력
print(len(counts))

# 각 단지의 집의 수 오름차순으로 정렬하여 출력
counts.sort()
for count in counts:
    print(count)
