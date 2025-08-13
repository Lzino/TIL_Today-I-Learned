# https://school.programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    MOD = 1000000007
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1          # |  (세로 1개)
    dp[2] = 2          # || , ==  (두 가지)
    
    # 점화식: dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    
    return dp[n]
