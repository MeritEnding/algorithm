from collections import defaultdict
def solution(tickets):
    graph=defaultdict(list)

    for start,end in tickets:
        graph[start].append(end)

    for key in graph:
        graph[key].sort(reverse=True)

    route=[]

    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop())
        route.append(start)
    
    dfs("ICN")

    return route[::-1]

    