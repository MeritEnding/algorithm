# 입력 받기
a, b = map(int, input().split())  # a: 학생 수, b: 최대 합격 가능 인원 수
ary = list(map(int, input().split()))  # 각 학생의 점수 리스트

# 초기값 설정
max_p = min(ary) - 1  # 커트라인으로 가능한 값이 없을 경우 대비 (최저 점수보다 1 낮은 값)
max_pass = 0  # 최대 합격자 수

# 가능한 커트라인 P(1~100)를 모두 시도해 본다
for p in ary:
    passed = [False] * a  # 각 학생의 합격 여부를 저장하는 리스트

    # 1차 합격: 커트라인 이상인 학생은 합격
    for i in range(a):
        if ary[i] >= p:
            passed[i] = True

    # 2차 합격: 커트라인 미달이지만, 인접한 학생 중 합격자가 있으면 합격
    for i in range(a):
        if not passed[i]:
            # 왼쪽이나 오른쪽 인접한 학생이 합격한 경우
            if (i > 0 and passed[i - 1]) or (i < a - 1 and passed[i + 1]):
                passed[i] = True

    # 현재 커트라인에서의 총 합격자 수
    total_pass = sum(passed)

    # 조건을 만족하면 최대 합격자 수와 커트라인 P를 갱신
    if total_pass <= b:
        # 더 많은 학생이 합격하거나,
        # 합격자 수가 같고 P가 더 큰 경우 갱신
        if total_pass > max_pass or (total_pass == max_pass and p > max_p):
            max_pass = total_pass
            max_p = p

# 최적의 커트라인 출력
print(max_p)
