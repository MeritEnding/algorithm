def solution(n,lost,reserve):
    # 도난 당했지만 여벌이 없는 학생과 여벌을 가지고 있지만 도난 당하지않은 학생을 분리
    net_lost =set(lost)-set(reserve)
    net_reserve=set(reserve)-set(lost)

    # 초기 수업 가능 학생 수 계산
    answer= n-len(net_lost)
    # 체육복을 빌려줄 수 있는지 확인
    for i in sorted(net_lost):
        if i-1 in net_reserve:
            net_reserve.remove(i-1)
            answer+=1
        elif i+1 in net_reserve:
            net_reserve.remove(i+1)
            answer+=1

    return answer

