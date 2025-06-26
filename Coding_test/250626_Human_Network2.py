# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18P2B6Iu8CFAZN
"""
1263. 사람 네트워크2 (SWEA)

목표 : 모든 노드 i의 Closeness Centrality
       CC(i) = Σ_j dist(i, j)  (j == i 제외)
       → CC 값이 가장 작은 노드의 합만 출력

전략 : 인접행렬이 이미 주어지므로
       O(N³)의 플로이드-워셜(Floyd-Warshall)로
       모든 쌍 최단거리(G[i][j])를 구한다.
"""

########## 상수 & 헬퍼 ##########
INF = 10**9        # '도달 불가능'을 나타내는 충분히 큰 값

def floyd_warshall(dist: list[list[int]], n: int) -> None:
    """
    dist : N×N 인접행렬 (제자리에서 최단거리로 덮어씀)
    n    : 노드 수
    """
    # 1) 0(간선 없음) ↔︎ INF 치환, 단 자기자신은 0 유지
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = INF

    # 2) 플로이드-워셜
    #     k : 중간 노드
    #     i : 출발 노드
    #     j : 도착 노드
    for k in range(n):
        for i in range(n):
            # 이미 dist[i][k]가 INF면 건너뛰어도 되지만
            # 분기처리보다 단순한 3중 루프가 더 빠름 (파이썬 기준)
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


########## 메인 ##########
T = int(input())    # 테스트케이스 수

for tc in range(1, T + 1):
    # ── 1. 입력 한 줄 파싱 ─────────────────────────────
    raw = list(map(int, input().split()))
    N   = raw[0]           # 노드 수
    raw = raw[1:]          # 나머지는 인접행렬 요소 N²개

    # ── 2. 1차원 → 2차원 인접행렬로 변환 ─────────────
    graph = [raw[i*N : (i+1)*N] for i in range(N)]

    # ── 3. 모든 쌍 최단거리 계산 ────────────────────
    floyd_warshall(graph, N)

    # ── 4. 노드별 CC 값 = 행(=dist 배열) 합 ─────────
    answer = min(sum(row) for row in graph)

    # ── 5. 결과 출력 ───────────────────────────────
    print(f"#%d %d" % (tc, answer))
