# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def day_return(date):
    # "YYYY.MM.DD" → 절대 일수(모든 달 = 28일 가정)
    y = int(date[:4]); m = int(date[5:7]); d = int(date[8:10])
    return (y * 12 + m) * 28 + d

def solution(today, terms, privacies):
    today_days = day_return(today)

    # 1) terms 사전: {'A': 6, 'B': 12, ...}
    term_dict = {}
    for t in terms:
        k, months = t.split()          # 예: "A 6" → ("A","6")
        term_dict[k] = int(months)

    # 2) 각 privacy의 만료 기준일 계산
    expire_days = []
    for p in privacies:
        date_str, key = p.split()      # 예: "2021.05.02 A" → ("2021.05.02","A")
        start = day_return(date_str)
        expire = start + term_dict[key] * 28   # 유효기간 끝 다음날(=만료 기준일)
        expire_days.append(expire)

    # 3) 오늘이 만료 기준일 이상이면 파기
    answer = []
    for idx, exp in enumerate(expire_days):
        if today_days >= exp:          # 만료됨 → 파기 대상
            answer.append(idx+1)

    return answer
