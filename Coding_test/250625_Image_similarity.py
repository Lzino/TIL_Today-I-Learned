def lcs_similarity(x: str, y: str) -> float:
    n = len(x)
    # (n+1) × (n+1) DP 테이블 0으로 초기화
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 표 채우기
    for i in range(1, n + 1):          # X의 i번째 문자까지
        for j in range(1, n + 1):      # Y의 j번째 문자까지
            if x[i - 1] == y[j - 1]:   # 글자 일치(↖)
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:                      # 글자 불일치(↑, ← 중 큰 값)
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 길이 → 유사도(%) 계산
    return dp[n][n] * 100.0 / n


# ---------------- 실행부 ----------------
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = input().strip()
    Y = input().strip()

    similarity = lcs_similarity(X, Y)
    print(f"#{tc} {similarity:.2f}")
