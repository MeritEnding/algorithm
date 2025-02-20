from collections import deque
def bfs(start, tree, visited, wire):
    
    queue =deque([start])
    visited[start]=True
    cnt=1
    while queue:
        now =queue.popleft()
        
        for neighbor in tree[now]:
            if (now == wire[0] and neighbor == wire[1]) or (now == wire[1] and neighbor == wire[0]):
                continue
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True
                cnt+=1
    return cnt
    


def solution(n, wires):
    answer = float("inf")
    tree =[[] for _ in range(n+1)]
    
    for a,b in wires:
        tree[a].append(b)
        tree[b].append(a)
        
    for wire in wires:
        visited=[False]*(n+1)
        cnt1 = bfs(wire[0], tree, visited, wire)
        cnt2 = n -cnt1
        answer = min(answer, abs(cnt1-cnt2))
    return answer
    