from collections import deque

def bfs(start, tree, visited, wire):
    queue = deque([start])
    visited[start] = True
    cnt = 1  # 시작 노드 포함

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            # wire[0] ↔ wire[1] 전선을 끊었으므로 탐색 제외
            if (node == wire[0] and neighbor == wire[1]) or (node == wire[1] and neighbor == wire[0]):
                continue
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                cnt += 1

    return cnt


def solution(n, wires):
    answer = float("inf")  # 최소값을 구하기 위한 초기값
    tree = [[] for _ in range(n + 1)]

    # 그래프 구성
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    for wire in wires:
        visited = [False] * (n + 1)
        cnt1 = bfs(wire[0], tree, visited, wire)  # 첫 번째 네트워크 개수
        cnt2 = n - cnt1  # 전체에서 빼면 두 번째 네트워크 개수

        answer = min(answer, abs(cnt1 - cnt2))  # 최소 차이 갱신

    return answer
