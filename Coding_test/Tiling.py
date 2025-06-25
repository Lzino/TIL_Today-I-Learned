# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWI8A_hqZ70DFAUH

MAX_N = 250
dp = [0]*(MAX_N+1)
dp[0], dp[1] = 1, 1

'''
핵심 로직 
- 피보나치 수열의 확장버전
- 피보나치는 다음 단계를 넘어가기 위한 경우의 수가 2개지만 
- 해당 문제는 3개씩 존재 
- 예시 : T(3) = 'T(2)에서 확장 방법 : 세로 그래프 1개' + 'T(1)에서 확장 방법 : 2X2 그래프. 1X2 가로 그래프 2개'
즉, 2개 차이날땐 방법 2가지, 1개 차이날땐 방법 1가지라서 T(N) = T(N-1) + 2*T(N-2)라는 점화식이 만들어짐
'''
for n in range(2, MAX_N+1):
    dp[n] = dp[n-1] + 2*dp[n-2]     # 점화식

T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    print(f"#{tc} {dp[N]}")
