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
def extract_matrices_dfs(grid, n):
    # 방문 여부를 체크할 2차원 배열 초기화
    visited = [[False] * n for _ in range(n)]
    matrices = []  # 발견한 submatrix의 (행, 열)을 저장할 리스트

    # DFS 함수 정의: 연결된 화학 용기(0이 아닌 값)를 찾아 cells에 저장
    def dfs(r, c, cells):
        visited[r][c] = True  # 현재 위치 방문 처리
        cells.append((r, c))  # 현재 위치를 영역에 추가

        # 4방향 탐색 (상, 하, 좌, 우)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            # 격자 범위 안이고, 아직 방문하지 않았고, 0이 아닌 값이면 DFS 계속
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and grid[nr][nc] != 0:
                    dfs(nr, nc, cells)

    # 전체 격자를 순회하면서 새로운 submatrix의 시작점을 찾음
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0 and not visited[i][j]:
                cells = []             # 하나의 submatrix를 구성하는 셀들을 저장
                dfs(i, j, cells)       # DFS로 연결된 블럭을 탐색

                # 사각형의 범위를 계산 (min/max 좌표)
                min_r = min(x[0] for x in cells)
                max_r = max(x[0] for x in cells)
                min_c = min(x[1] for x in cells)
                max_c = max(x[1] for x in cells)

                # 사각형의 행과 열 길이 계산
                height = max_r - min_r + 1
                width = max_c - min_c + 1
                matrices.append((height, width))  # 크기 정보 저장

    return matrices  # 모든 submatrix의 크기 반환


def reconstruct_chain(matrices):
    # 각 matrix를 (행, 열) 쌍으로 생각하고 연결 사슬 형태로 정렬
    # ABC 행렬곱이라고 했을때 어떤 행렬이 A번째 행렬이 될지 찾는 것. 연결이 안되는 것부터 시작하기. 
    info_dict = {r: c for r, c in matrices}  # 행 → 열 매핑
    keys = set(info_dict.keys())            # 시작 노드들
    values = set(info_dict.values())        # 끝 노드들

    # 시작점 찾기: 다른 노드가 가리키지 않는 노드 (맨 처음에 오는 행 크기)
    start = (keys - values).pop()
    '''
    keys = set(info_dict.keys())     # 시작노드만 모은 것 → {'a', 'b', 'c'}
    values = set(info_dict.values()) # 끝노드 모은 것   → {'b', 'c', 'd'}
    start = (keys - values).pop()    # 시작노드 → 'a'
    '''

    sorted_matrices = []  # 정렬된 순서의 (행, 열) 리스트

    # 사슬을 따라가며 정렬된 순서대로 리스트를 구성
    while len(sorted_matrices) < len(matrices):
        sorted_matrices.append((start, info_dict[start]))  # 현재 노드 추가
        start = info_dict[start]  # 다음 노드로 이동

    return sorted_matrices  # 정렬된 행렬 리스트 반환


def matrix_chain_order(matrices):
    n = len(matrices)
    dp = [[0] * n for _ in range(n)]  # DP 테이블 초기화

    # 곱셈 연산 계산을 위해 필요한 차원 배열 생성
    dims = [matrices[0][0]] + [m[1] for m in matrices]
    # 예: [(10, 100), (100, 5), (5, 50)] → dims = [10, 100, 5, 50]

    # 행렬 체인 곱셈 DP: 길이 2부터 시작해서 점차 확장
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')  # 최소값을 찾기 위해 초기값 무한대로 설정
            for k in range(i, j):
                '''
                분할 지점 k를 기준으로 좌/우 영역 비용 + 곱셈 비용 계산
                예시 (AB)C 
                - dp[i][k] = (AB)의 계산
                - dp[k + 1][j] = C의 계산
                - dims[i] * dims[k + 1] * dims[j + 1] = (AB)C의 전체 계
                '''
                cost = (dp[i][k] + dp[k + 1][j] +
                    dims[i] * dims[k + 1] * dims[j + 1])
                dp[i][j] = min(dp[i][j], cost)  # 최소값 갱신

    return dp[0][n - 1]  # 전체 곱셈 최소 연산 수 반환


# ========================
# 메인 실행 코드
# ========================

T = int(input())  # 테스트 케이스 수 입력

for test_case in range(1, T + 1):
    n = int(input())  # 격자 크기
    grid = [list(map(int, input().split())) for _ in range(n)]  # 격자 데이터 입력

    matrices = extract_matrices_dfs(grid, n)        # 1. submatrix들 찾기
    sorted_matrices = reconstruct_chain(matrices)   # 2. 올바른 순서로 정렬
    result = matrix_chain_order(sorted_matrices)    # 3. 최소 곱셈 연산 계산

    print(f"#{test_case} {result}")  # 결과 출력

'''
# ======== C ++ 버전 ======== 
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <climits>
using namespace std;

int n;
vector<vector<int>> grid;
vector<vector<bool>> visited;
vector<pair<int, int>> matrices;

// 방향 벡터 (상, 하, 좌, 우)
int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

// DFS로 하나의 submatrix 영역을 찾는다
void dfs(int r, int c, vector<pair<int, int>>& cells) {
    visited[r][c] = true;
    cells.push_back({r, c});

    for (int d = 0; d < 4; d++) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
            if (!visited[nr][nc] && grid[nr][nc] != 0) {
                dfs(nr, nc, cells);
            }
        }
    }
}

// 1. submatrix 추출
void extract_matrices_dfs() {
    visited.assign(n, vector<bool>(n, false));
    matrices.clear();

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != 0 && !visited[i][j]) {
                vector<pair<int, int>> cells;
                dfs(i, j, cells);

                int min_r = n, max_r = 0, min_c = n, max_c = 0;
                for (auto cell : cells) {
                    min_r = min(min_r, cell.first);
                    max_r = max(max_r, cell.first);
                    min_c = min(min_c, cell.second);
                    max_c = max(max_c, cell.second);
                }

                int height = max_r - min_r + 1;
                int width = max_c - min_c + 1;
                matrices.push_back({height, width});
            }
        }
    }
}

// 2. 연결 사슬 정렬
vector<pair<int, int>> reconstruct_chain(const vector<pair<int, int>>& matrices) {
    map<int, int> info_map;
    set<int> keys, values;

    for (auto p : matrices) {
        info_map[p.first] = p.second;
        keys.insert(p.first);
        values.insert(p.second);
    }

    // 시작점: keys - values
    int start;
    for (int k : keys) {
        if (values.count(k) == 0) {
            start = k;
            break;
        }
    }

    vector<pair<int, int>> sorted_matrices;
    while (sorted_matrices.size() < matrices.size()) {
        int next = info_map[start];
        sorted_matrices.push_back({start, next});
        start = next;
    }

    return sorted_matrices;
}

// 3. 행렬 곱 최소 연산 계산 (DP)
int matrix_chain_order(const vector<pair<int, int>>& matrices) {
    int n = matrices.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    vector<int> dims(n + 1);

    dims[0] = matrices[0].first;
    for (int i = 0; i < n; i++) {
        dims[i + 1] = matrices[i].second;
    }

    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            dp[i][j] = INT_MAX;

            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k + 1][j]
                         + dims[i] * dims[k + 1] * dims[j + 1];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }

    return dp[0][n - 1];
}

// ========================
// 메인 함수
// ========================
int main() {
    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++) {
        cin >> n;
        grid.assign(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> grid[i][j];
            }
        }

        extract_matrices_dfs(); // 1. submatrix 추출
        auto sorted_matrices = reconstruct_chain(matrices); // 2. 정렬
        int result = matrix_chain_order(sorted_matrices); // 3. DP로 최소 곱셈

        cout << "#" << test_case << " " << result << endl;
    }

    return 0;
}
'''
'''
# ======== JAVA 버전 ======== 
import java.util.*;

public class MatrixChainSolver {
    static int n;
    static int[][] grid;
    static boolean[][] visited;
    static List<int[]> matrices = new ArrayList<>();

    // 방향 벡터: 상, 하, 좌, 우
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    // DFS로 하나의 submatrix 영역 탐색
    static void dfs(int r, int c, List<int[]> cells) {
        visited[r][c] = true;
        cells.add(new int[]{r, c});

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                if (!visited[nr][nc] && grid[nr][nc] != 0) {
                    dfs(nr, nc, cells);
                }
            }
        }
    }

    // 1. DFS로 submatrix 추출
    static void extractMatricesDFS() {
        visited = new boolean[n][n];
        matrices.clear();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0 && !visited[i][j]) {
                    List<int[]> cells = new ArrayList<>();
                    dfs(i, j, cells);

                    int minR = n, maxR = 0, minC = n, maxC = 0;
                    for (int[] cell : cells) {
                        minR = Math.min(minR, cell[0]);
                        maxR = Math.max(maxR, cell[0]);
                        minC = Math.min(minC, cell[1]);
                        maxC = Math.max(maxC, cell[1]);
                    }

                    int height = maxR - minR + 1;
                    int width = maxC - minC + 1;
                    matrices.add(new int[]{height, width});
                }
            }
        }
    }

    // 2. from → to 사슬 구조로 정렬
    static List<int[]> reconstructChain(List<int[]> matrices) {
        Map<Integer, Integer> infoMap = new HashMap<>();
        Set<Integer> keys = new HashSet<>();
        Set<Integer> values = new HashSet<>();

        for (int[] mat : matrices) {
            infoMap.put(mat[0], mat[1]);
            keys.add(mat[0]);
            values.add(mat[1]);
        }

        // 시작점 찾기: keys - values
        int start = -1;
        for (int k : keys) {
            if (!values.contains(k)) {
                start = k;
                break;
            }
        }

        List<int[]> sorted = new ArrayList<>();
        while (sorted.size() < matrices.size()) {
            int next = infoMap.get(start);
            sorted.add(new int[]{start, next});
            start = next;
        }

        return sorted;
    }

    // 3. DP로 최소 행렬 곱 계산
    static int matrixChainOrder(List<int[]> matrices) {
        int size = matrices.size();
        int[][] dp = new int[size][size];
        int[] dims = new int[size + 1];

        dims[0] = matrices.get(0)[0];
        for (int i = 0; i < size; i++) {
            dims[i + 1] = matrices.get(i)[1];
        }

        for (int length = 2; length <= size; length++) {
            for (int i = 0; i <= size - length; i++) {
                int j = i + length - 1;
                dp[i][j] = Integer.MAX_VALUE;

                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k + 1][j] +
                            dims[i] * dims[k + 1] * dims[j + 1];
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }
        }

        return dp[0][size - 1];
    }

    // ========================
    // Main 메서드
    // ========================
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            n = Integer.parseInt(sc.nextLine());
            grid = new int[n][n];

            for (int i = 0; i < n; i++) {
                String[] tokens = sc.nextLine().split(" ");
                for (int j = 0; j < n; j++) {
                    grid[i][j] = Integer.parseInt(tokens[j]);
                }
            }

            extractMatricesDFS();                          // 1. submatrix 추출
            List<int[]> sortedMatrices = reconstructChain(matrices);  // 2. 정렬
            int result = matrixChainOrder(sortedMatrices);            // 3. 최소 곱셈 연산

            System.out.println("#" + testCase + " " + result);
        }

        sc.close();
    }
}

'''

