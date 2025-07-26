# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque

def solution(queue1, queue2):
	q1 = deque(queue1)
	q2 = deque(queue2)

	s1, s2 = sum(q1), sum(q2)
	total = s1 + s2

	# 두 수의 합이 홀수 일 때 같은 값이 안나옴 
	if total % 2 != 0:
		return -1

	# 평균으로 타겟 만들기
	target = total // 2
	# 최악 가정 (실험상 3번)
	max_count = len(queue1) * 3

	count = 0 

	while count <= max_count:
		if s1 == target:
			return count

		# q1이 평균보다 큰 경우
		elif s1 > target :
			num = q1.popleft() # 맨 앞의 원소 POP 
			s1 -= num # 큐 1 합에서 빼기
			q2.append(num) # 큐 2 뒤에 추가
			s2 += num # 큐 2 합에 추가 

		# q2가 평균보다 큰 경우
		else :
			num = q2.popleft()
			s2 -= num
			q1.append(num)
			s1 += num

		count += 1
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
