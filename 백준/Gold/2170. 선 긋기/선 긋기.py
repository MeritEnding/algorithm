import sys

input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

lines.sort()  # 선을 시작점 기준으로 정렬

merged_start, merged_end = lines[0]  # 첫 번째 구간의 시작과 끝

total_length = 0
for i in range(1, N):  # 나머지 선들 보자
    current_start, current_end = lines[i]

    # 겹치는 경우
    if merged_end >= current_start:
        merged_end = max(merged_end, current_end)  # 겹치는 구간이 있으면 끝점을 확장
    else:
        total_length += (merged_end - merged_start)  # 겹치지 않으면 기존 구간 길이 더하고
        merged_start, merged_end = current_start, current_end  # 새로운 구간으로 업데이트

# 마지막 남은 구간의 길이 더하기
total_length += (merged_end - merged_start)

print(total_length)
