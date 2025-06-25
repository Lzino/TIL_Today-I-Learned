# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18Q_MqIvUCFAZN

def lcs_similarity(x: str, y: str) -> float:
    n = len(x)
    # 메모리를 줄이기 위해 행 2개만 사용
    prev = [0] * (n + 1)   # dp[i-1][*]
    curr = [0] * (n + 1)   # dp[i][*]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = prev[j] if prev[j] > curr[j - 1] else curr[j - 1]
        prev, curr = curr, [0] * (n + 1)   # 다음 행 준비

    return prev[n] * 100.0 / n             # LCS 길이 / 전체길이 * 100


T = int(input())
for tc in range(1, T + 1):
    N = int(input())           # 문자열 길이 (문제 보장: X, Y 모두 N글자)
    X = input().strip()
    Y = input().strip()

    similarity = lcs_similarity(X, Y)
    # 소수점 둘째 자리까지 출력
    print(f"#{tc} {similarity:.2f}")
