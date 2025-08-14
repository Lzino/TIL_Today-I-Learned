# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
	MOD = 1000000007
	blocked = set(map(tuple, puddles))
	dp = [0] * (m + 1)
	dp[1] = 1 # 시작점 (1,1)

	# (x, y) 쌍으로 루프를 돌리며 검색 
	for y in range(1, n+1):
		for x in range (1, m + 1):
			if (x, y) in blocked:
				dp[x] = 0
			else : 
				dp[x] = (dp[x] + dp[x-1]) % MOD

	return dp[m]
