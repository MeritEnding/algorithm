N = int(input())
applicants = [tuple(map(int, input().split())) for _ in range(N)]

ranks = []
for i in range(N):
    rank = 1  # 시작 등수는 1등
    for j in range(N):
        if i == j:
            continue
        # i보다 j가 서류/면접 모두 높으면 등수 밀림
        if applicants[j][0] > applicants[i][0] and applicants[j][1] > applicants[i][1]:
            rank += 1
    ranks.append(rank)

print(' '.join(map(str, ranks)))
