# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque

def solution(queue1, queue2):
    # Python 리스트를 큐처럼 O(1)로 pop/append 하려면 deque가 적합
    q1 = deque(queue1)
    q2 = deque(queue2)

    # 각 큐의 합과 전체 합
    s1, s2 = sum(q1), sum(q2)
    total = s1 + s2

    # 전체 합이 홀수면 두 큐를 같은 합으로 만드는 것이 원천적으로 불가능
    if total % 2 != 0:
        return -1

    # 두 큐가 도달해야 할 목표 합 (동일해야 하는 합)
    target = total // 2

    # 안전장치: 무한 루프 방지용 최대 연산 횟수(상한)
    # 2번 돌리면 TC에 걸려서 3번 돌리는걸로 최적화 
    max_count = len(queue1) * 3

    count = 0  # 현재까지 수행한 작업(= pop 1회 + insert 1회)의 횟수

    # 핵심 아이디어:
    # s1(큐1의 합)이 target보다 크면, 큐1에서 pop하여 큐2로 옮겨 s1을 줄임
    # s1이 target보다 작으면, 큐2에서 pop하여 큐1로 옮겨 s1을 늘림
    # s1 == target이 되는 순간이 정답(가장 먼저 도달하는 순간이 최소 횟수)
    while count <= max_count:
        if s1 == target:
            return count

        elif s1 > target:
            # 큐1의 합이 너무 크므로, 큐1의 맨 앞을 꺼내 큐2 뒤에 붙인다
            num = q1.popleft()  # pop
            s1 -= num           # s1 감소
            q2.append(num)      # insert
            s2 += num           # s2 증가

        else:  # s1 < target
            # 큐1의 합이 작으므로, 큐2의 맨 앞을 꺼내 큐1 뒤에 붙인다
            num = q2.popleft()  # pop
            s2 -= num           # s2 감소
            q1.append(num)      # insert
            s1 += num           # s1 증가

        count += 1  # 작업 1회 완료(pop+insert를 한 번으로 센다)

    # 상한 횟수 내에 목표 합을 만들지 못했다면 불가능 판정
    return -1

'''
[C ++ 버전]
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>  // accumulate 함수용

using namespace std;

int solution(vector<int> queue1, vector<int> queue2) {
    queue<int> q1, q2;

    // 초기 큐 구성
    for (int n : queue1) q1.push(n);
    for (int n : queue2) q2.push(n);

    long long sum1 = accumulate(queue1.begin(), queue1.end(), 0LL);  // 큐1의 합
    long long sum2 = accumulate(queue2.begin(), queue2.end(), 0LL);  // 큐2의 합
    long long total = sum1 + sum2;

    // 전체 합이 홀수면 절대 불가능
    if (total % 2 != 0) return -1;

    long long target = total / 2;

    int maxCount = queue1.size() * 3;  // 최대 반복 허용치
    int count = 0;

    // 큐에서 pop한 값 추적용
    // 참고: queue는 순회가 불편하므로 직접 push/pop 필요
    while (count <= maxCount) {
        if (sum1 == target) return count;  // 정답

        if (sum1 > target) {
            // 큐1에서 값 빼서 큐2에 넣기
            if (q1.empty()) return -1;
            int num = q1.front(); 
            q1.pop();
            sum1 -= num;
            q2.push(num);
            sum2 += num;
        } else {
            // 큐2에서 값 빼서 큐1에 넣기
            if (q2.empty()) return -1;
            int num = q2.front(); 
            q2.pop();
            sum2 -= num;
            q1.push(num);
            sum1 += num;
        }
        count++;
    }

    // 최대 횟수 초과 시 불가능
    return -1;
}


'''
