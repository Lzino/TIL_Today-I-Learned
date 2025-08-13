# https://school.programmers.co.kr/learn/courses/30/lessons/72413

def solution(n, s, a, b, fares):
    """
    n  : 지점(노드) 수 (1..n)
    s  : 출발 지점
    a  : A의 도착 지점
    b  : B의 도착 지점
    fares: [u, v, w] 형식의 간선 정보 (양방향, 비용 w)

    반환값: s에서 출발하여 A, B가 각각 도착하는 최소 택시 요금
    """

    # ------------------------------------------------------------
    # 1) 거리 테이블 초기화
    # ------------------------------------------------------------
    # 최악 비용 상한: 간선 최댓값 100,000 * (최대 간선 수 199) ≪ 1e15
    INF = 10**15

    # dist[i][j] = i -> j 최단 거리
    # 노드가 1..n이므로, 편하게 인덱스 0을 버리고 (n+1) x (n+1) 사용
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0
    for i in range(1, n + 1):
        dist[i][i] = 0

    # 간선(양방향) 비용 채우기
    for u, v, w in fares:
        # 혹시 더 작은 비용이 들어오면 갱신 (문제 조건상 중복은 없지만 방어적으로)
        if w < dist[u][v]:
            dist[u][v] = w
            dist[v][u] = w

    # ------------------------------------------------------------
    # 2) 플로이드-워셜: 모든 쌍 최단거리 구하기
    #    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 를
    #    모든 k(중간 경유지)에 대해 반영
    # ------------------------------------------------------------
    for mid in range(1, n + 1):          # 중간 경유지 k
        for start in range(1, n + 1):    # 출발 i
            if dist[start][mid] == INF:   # i->k 경로가 없으면 j를 돌 필요 없음 (가지치기)
                continue
            for end in range(1, n + 1):  # 도착 j
                if dist[mid][end] == INF:  # k->j 경로가 없으면 스킵
                    continue
                # i->j 기존값 vs i->k + k->j 경유값
                new_cost = dist[start][mid] + dist[mid][end]
                if new_cost < dist[start][end]:
                    dist[start][end] = new_cost

    # ------------------------------------------------------------
    # 3) 합승 분기점 k를 모두 시도
    #    S->k는 함께, k->A / k->B는 각자 이동.
    #    k = s 이면 "합승 없이 각자" 케이스도 자동 포함됨.
    # ------------------------------------------------------------
    answer = min(
        dist[s][k] + dist[k][a] + dist[k][b]
        for k in range(1, n + 1)
    )

    return answer
