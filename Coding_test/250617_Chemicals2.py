# 화학물질2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18OR16IuUCFAZN

'''
로직
- 2가지의 조건이 있다.
- 1번째는 그래프 안에서 영역을 찾는 과정이므로 DFS, BFS를 사용하면 된다.
- 2번째 조건이 까다로운데,
  행렬곱을 DP로 풀어야한다. 그리고 최소로 적은 계산수를 만들어야한다.
  그리고 행렬곱은 맞닿아 있는 크기가 맞아야 곱셈이 가능해진다.
- 일단 DFS를 만들고 DP를 어떻게 적용할지 고민하는 것이 좋다.
- 왼쪽 행렬곱 + 오른쪽 행렬곱 + 둘 합칠때 비용 을 만들어내는게 난이도가 상승하는 부분
'''
def extract_matrices(grid, n):
    visited = [[False] * n for _ in range (n)]
    matrix = []

    def dfs(r,c, cells):
        # 방문체크
        visited[r][c] = True
        cells.append(r, c)

        for dr, dc in [(1,0),(-1,0), (0,1), (0,-1)]:
            # 이동했을때
            nc, nr = r + dr, c + dc
            # 만약 이동한 게 0보단 크고 n보단 작을때(?)
            if 0 <= nr < n and 0 <= nc < n :
                # 방문한적이 없고 gird가 0이 아니면
                if not visited[nr][nc] and grid[nr][nc] != 0:
                    dfs(nr, nc, cells)

    for i in range(n):
        for j in range(n):
            # 만약 그리드가 0이 아니고 방문 하지 않았으면 DFS 실행
            if grid[i][j] != 0 and not visited[i][j]:
                cells = []
                dfs(i, j, cells)

        for i in range(n):
            for j in range(n):
                if grid[i][j] !=0 and not visited[i][j]:
                    cells = []
                    dfs(i, j, cells)

                    # DFS가 끝나고 범위 계산
                    min_r = min(x[0] for x in cells)
                    max_r = max(x[0] for x in cells)
                    min_c = min(x[1] for x in cells)
                    max_c  = max(x[1] for x in cells)

                    height = max_r - min_r + 1
                    width = max_c - min_c + 1

                    matrix.append((height, width))
        return matrices

    def bfs (r,c):
        h, w = 0, 0

        # 세로 길이 계산
        i = r
        while i < n and grid[i][c] != 0 :
            i += 1
        h = i - r

        # 가로 길이 계산
        j = c
        while j < n and grid[r][j] != 0:
            j += 1
        w = j - c

        for i in range (r, r + h):
            for j in range(c, c + w):
                visited[i][j] = True

        return (h,w)

    for i in range(n):
        for j in range(n):
            if not visited[nr][nc] and grid[nr][nc] != 0:
                matrix.append(bfs(i,j))

    def reconstruct_chain(matrix):
        # 연결 사슬을 만들어서 올바른 순서로 정렬
        info_dict = {r: c for r, c in matrix}
        keys = set(info_dict.keys())
        values = set(info_dict.values())

        start = (keys - values).pop()
        sorted_matrices = []

        while len(sorted_matrices) < len(matrix):
            sorted_matrices.append((start, info_dict[start]))
            start = info_dict[start]

        return sorted_matrices

    def matrix_chain_order(matrix):
        n = len(matrix)
        dp = [[0] * n for _ in range (n)]
        dims = [matrix[0][0]] + [m[1] for m in matrix]

        for length in range(2, n +1 ):
            for i in range(n - lenght + 1):
                j = i + length - 1
                dp[i][j] = float('-inf')
                for k in range(i, j):
                    #왼쪽 행렬곱 + 오른쪽 행렬곱 + 둘 합칠때 비용
                    cost = (dp[i][k] + dp[k+1][j] + dim[i]*dim[k+1]*dim[j+1])
                    # dp로 업데이트하면서 최소값 갱신
                    dp[i][j] = min(dp[i][j], cost)
        return dp[0][n-1]
    
# 메인 코드
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    matrix = extract_matrices_dfs(grid, n)
    sorted_matrices = reconstruct_chain(matrix)
    result = matrix_chain_order(sorted_matrices)

    print(f"#{test_case} {result}")
