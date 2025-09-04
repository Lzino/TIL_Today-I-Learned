### 그래프 ####

# BFS (격자) : 2차원 맵에서 최단거리 탐색
# 예시:
# grid = [
#     [1,1,0],
#     [1,1,1],
#     [0,1,1]
# ]  # 1=이동 가능, 0=이동 불가
# bfs_grid(grid, 0, 0) → 시작 (0,0)에서 각 칸까지의 최단거리 행렬
from collections import deque

# 4방향 이동(아래, 위, 오른쪽, 왼쪽)
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs_grid(grid, sy, sx):
    """
    grid : 2차원 리스트(행렬). 이동 가능이면 1(True), 벽/불가면 0(False)
    sy,sx: 시작 좌표 (row, col)
    return: 시작점에서 각 칸까지의 '최단 거리'를 담은 2차원 리스트
            도달 불가 칸은 -1
    """
    n, m = len(grid), len(grid[0])          # n=행(세로 크기), m=열(가로 크기)
    dist = [[-1]*m for _ in range(n)]       # 방문표시 겸 거리 저장(-1이면 미방문/도달불가)
    q = deque([(sy, sx)])                   # BFS용 큐에 시작점 삽입
    dist[sy][sx] = 0                        # 시작점까지의 거리는 0

    # 큐가 빌 때까지 반복 (BFS: 가까운 칸부터 레벨 순서대로 확장)
    while q:
        y, x = q.popleft()                  # 현재 칸을 꺼냄(FIFO)
        # 4방향 이웃 칸을 확인
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 1) 범위 안  2) 통로(이동 가능)  3) 아직 방문 안 함
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1   # 최단거리 갱신(부모거리 + 1)
                q.append((ny, nx))              # 다음 확장을 위해 큐에 추가

    return dist


# BFS (무가중치, 인접리스트) : 노드 번호 기반 최단거리 탐색
# 예시:
# adj = [
#     [1,2],  # 0번 노드와 1,2번 연결
#     [0,3],
#     [0,1],
#     [3,4]
# ]
# bfs_adj(adj, 0) → [0, 1, 1, 2]
'''
결국 시작전에 길이, 거리 상태, 시작점과 시작점을 deque에 넣기 그리고 
popleft로 쌍으로 뱉게 한다음 거리 상태가 닿은적이 없으면 1 추가하고 
deque에 해당좌표 넣기
'''
from collections import deque
def bfs_adj(adj, s):
    n = len(adj)
    dist = [-1]*n
    q = deque([s])
    dist[s] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


# DFS (반복) : 스택으로 깊이우선 탐색
# 예시:
# adj = [
#     [1,2],
#     [0,3],
#     [0,3],
#     [1,2]
# ]
# dfs_adj(adj, 0) → 방문 순서 예: [0,2,3,1]
def dfs_adj(adj, s):
    n = len(adj)                     # 전체 노드 개수
    vis = [False]*n                   # 방문 여부를 기록하는 배열
    stack = [s]                       # DFS용 스택 (시작 노드를 넣고 시작)
    order = []                        # 방문 순서를 기록하는 리스트

    while stack:                      # 스택이 빌 때까지 반복
        u = stack.pop()               # 스택의 마지막 요소(현재 노드) 꺼내기
        if vis[u]: continue           # 이미 방문한 노드면 건너뛰기
        vis[u] = True                 # 현재 노드를 방문 표시
        order.append(u)               # 방문 순서 기록
        for v in adj[u]:              # 현재 노드에 연결된 모든 이웃 노드 순회
            if not vis[v]:            # 아직 방문 안 했다면
                stack.append(v)       # 스택에 추가 (나중에 탐색)
    return order                      # 전체 방문 순서 반환



# 다익스트라 (가중치 양수) : 한 시작점 → 모든 정점 최단거리
# 예시:
# adj_w = [
#     [(2,1),(5,2)], # 0 → 1(2), 2(5)
#     [(2,0),(3,2)],
#     [(5,0),(3,1)]
# ]
# dijkstra(adj_w, 0) → [0, 2, 5]
import heapq
def dijkstra(adj, start):
    INF = 10**15
    n = len(adj)
    dist = [INF]*n
    dist[start] = 0
    # (거리, 노드)
    pq = [(0, start)]                          
    # 힙이 빌 때까지 반복
    while pq:
        # 현재 힙에서 가장 작은 거리 d를 가진 노드 u
        d, u = heapq.heappop(pq)
        # 이미 더 짧은 거리 있으면
        if d > dist[u]: continue  
        for w, v in adj[u]:
            # u까지의 최단거리 d에 간선 가중치 w를 더해
            # u를 거쳐 v로 가는 후보 거리 nd를 계산
            nd = d + w
            # nd가 기존 v의 최단거리보다 더 짧다면 갱신
            if nd < dist[v]:
                dist[v] = nd
                # “v까지 nd 거리로 갈 수 있다”는 새로운 후보를 힙에 넣어
                # 추후에 가장 짧은 것부터 계속 처리
                heapq.heappush(pq, (nd, v))
    return dist
  

# 플로이드–워셜 : 모든 쌍 최단거리
# 예시:
# INF = 10**9
# dist = [
#     [0, 3, INF],
#     [3, 0, 1],
#     [INF, 1, 0]
# ]
# floyd_warshall(dist) → [[0, 3, 4], [3, 0, 1], [4, 1, 0]]
def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):                          # 경유 노드
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# 위상정렬 : 선후관계가 있는 DAG의 순서 정하기
# 예시:
# adj_dag = [
#     [1,2],  # 0 → 1, 2
#     [3],
#     [3],
#     []
# ]
# topo_sort(adj_dag) → [0, 1, 2, 3] 또는 [0, 2, 1, 3]
from collections import deque
def topo_sort(adj):
    n = len(adj)
    indegree = [0]*n
    order = []
    for u in range(n):
        for v in adj[u]:
            # indeg[v]: 정점 v로 들어오는 간선 수
            indegree[v] += 1
    # 들어오는 간선이 없는 정점을 일단 에 넣어 시작 
    q = deque([i for i in range(n) if indegree[i]==0])
    '''
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    '''
    while q:
        u = q.popleft()
        # 큐에서 하나 꺼낸 u를 순서에 기록
        order.append(u)
        for v in adj[u]:
            # u에서 나가는 모든 간선 u -> v를 제거하는 효과로 v의 진입차수를 1씩 감소
            indegree[v] -= 1
            # indeg[v]가 0이 되면 이제 선행 조건이 없으니 큐에 추가
            if indegree[v] == 0:
                q.append(v)
    return order


### DP ###
'''
배열 초기화 한 다음
초기 입력해야하는 값 만들고 
점화식 대입. 이때 범위 설정 주의
'''
# 1차원 : 예) 피보나치
# 예시: n=5, base0=0, base1=1 → [0, 1, 1, 2, 3, 5]
dp = [0]*(n+1)
dp[0], dp[1] = 0, 1 # base0, base1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]  # 점화식 수정


# 2차원 : 예) 격자 경로 수
# 예시: n=3, m=3, blocked={(2,2)}
# dp[3][3] 값이 (1,1)→(3,3)까지의 경로 수
dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = 1
for y in range(1, n+1):
    for x in range(1, m+1):
        if (x,y) in blocked: 
                continue
        if (x,y) != (1,1):
            dp[y][x] = dp[y-1][x] + dp[y][x-1]


def knapsack_01(N, weight, value):
    """
    0/1 Knapsack (아이템은 각 0개 또는 1개만 선택 가능)
    N: 배낭 용량 (int)
    weight, value: 같은 길이의 리스트. weight[i]는 i번째 아이템 무게(>=1), value[i]는 가치.

    반환: 용량 N에서 얻을 수 있는 최대 가치 (int)
    복잡도: 시간 O(nN), 공간 O(N)
    """
    assert len(weight) == len(value)
    n = len(weight)
    dp = [0] * (N + 1)  # dp[w]: 용량 w에서의 최대 가치

    for i in range(n):
        item_weight = weight[i]
        item_value = value[i]
        # 역순 순회: 같은 아이템을 한 번만 쓰도록 보장 (0/1 조건)
        for capacity in range(N, item_weight - 1, -1):
            # 안 담는 경우 vs 담는 경우(이전 상태 dp[capacity - item_weight]에서 가치 추가)
            dp[capacity] = max(dp[capacity],
                               dp[capacity - item_weight] + item_value)
    return dp[N]





# 카데인 (연속합 최대)
# 예시: arr=[-2,1,-3,4,-1,2,1] → max_sum=6
current_sum = arr[0]
max_sum = arr[0]
for num in arr[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

'''
첫번째 인덱스부터 특정 인덱스까지의 구간의 합을 미리 구하는 방
O(1)에 구간길이 구할수있음
예: arr = [1, 2, 3, 4]
구간합(1 ~ 3) → prefix[4] - prefix[1]
0~r → prefix[r+1]
q~r → prefix[r+1] - prefix[q]
'''
# 누적합 (Prefix Sum)
# 예시: arr=[1,2,3,4], prefix=[0,1,3,6,10]
# 구간합(1~3) = prefix[4] - prefix[1] = 9
prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]


# 이진 탐색
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:  # 탐색 구간이 남아있는 동안
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # 값 찾음 → 인덱스 반환
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽으로 범위 이동
        else:
            right = mid - 1  # 왼쪽으로 범위 이동
    
    return -1  # 못 찾으면 -1



# 이진탐색 (입국심사)
# 예시: immigration(6, [7, 10]) → 28
def immigration(n, times):
    left, right = 1, max(times) * n
    answer = right
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for t in times:
            people += mid // t
            if people >= n:  # 조기 종료
                break
        if people >= n:      # mid 시간 안에 처리 가능
            answer = mid
            right = mid - 1
        else:                # 시간 부족 → 늘려야 함
            left = mid + 1
    return answer
