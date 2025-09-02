# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    # 8개 성격 유형별 점수판 (초기값 0)
    scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    # 각 문항 처리
    for i in range(len(survey)):
        # survey[i]는 예: "RT" 혹은 "TR"
        # first : 비동의(1~3) 쪽에 점수를 받는 유형
        # second: 동의(5~7)  쪽에 점수를 받는 유형
        first, second = survey[i][0], survey[i][1]
        choice = choices[i]  # 1~7

        # 4(모르겠음)는 점수 없음 → 스킵
        if choice == 4:
            continue

        # 1/7 → 3점, 2/6 → 2점, 3/5 → 1점
        # 즉, 4에서 얼마나 떨어져 있는지의 절대값이 점수
        point = abs(4 - choice)

        if choice < 4:
            # 비동의 쪽(1~3) 선택 → first 유형이 점수 획득
            scores[first] += point
        else:
            # 동의 쪽(5~7) 선택 → second 유형이 점수 획득
            scores[second] += point

    # 4개 지표 쌍을 순서대로 판단하여 결과 문자열 구성
    result = ''
    for a, b in [('R','T'), ('C','F'), ('J','M'), ('A','N')]:
        # 점수가 같으면 사전순으로 빠른 쪽을 선택해야 하므로
        # >= 로 a를 우선 (문제의 규칙과 일치)
        if scores[a] >= scores[b]:
            result += a
        else:
            result += b
    
    return result
