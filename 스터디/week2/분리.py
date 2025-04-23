# 아파트 단지 수 입력
n = int(input())

apartments = []           # 각 아파트 정보를 저장할 리스트
total_population = 0      # 전체 주민 수

# 각 아파트 단지의 위치와 사람 수 입력
for idx in range(1, n + 1):
    position, people = map(int, input().split())
    # (위치, 사람 수, 입력 순서로 주어진 단지 번호)를 저장
    apartments.append((position, people, idx))
    total_population += people  # 전체 주민 수 누적

# 아파트를 위치 기준으로 오름차순 정렬
apartments.sort()

# 누적 인구수를 저장할 변수
cumulative = 0

# 위치가 작은 아파트부터 순회하며 누적 인구 계산
for pos, people, original_idx in apartments:
    cumulative += people  # 현재 단지의 사람 수를 누적

    # 누적 인구가 전체의 절반 이상이 되는 순간,
    # 그 단지의 번호가 최소 이동 거리의 조건을 만족함
    if cumulative >= total_population / 2:
        print(original_idx)  # 조건을 만족하는 단지 번호 출력
        break  # 더 이상 볼 필요 없으므로 종료
