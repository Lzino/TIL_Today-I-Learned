# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 시간 복잡도 : O(kn)
        results = []
        window = collections.deque()
        # 최소값으로 초기화
        current_max = float('-inf')
        for i , v in enumerate(nums):
            # 값 추가
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최대값보다 큰 경우
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            
            results.append(current_max)

            # 최대값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
        return results

    def mSW__Monotonic(self, nums: List[int], k: int) -> List[int]:
        # 시간 복잡도 : O(n)
        result = []
        dq = deque()  # 인덱스를 저장

        for i in range(len(nums)):
            # 1. 앞에서 범위 벗어난 인덱스 제거
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. 뒤에서 작거나 같은 값들 제거 (현재 값보다 작으면 필요 없음)
            # Monotonic Deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. 현재 인덱스 추가
            dq.append(i)

            # 4. 결과 추가 (윈도우가 만들어졌을 때부터)
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

'''
#include <deque>
using namespace std;

class MonotonicQueue {
private:
    deque<int> dq;

public:
    void push(int value) {
        // 뒷부분에서 자신보다 작은 값 제거
        while (!dq.empty() && dq.back() < value) {
            dq.pop_back();
        }
        dq.push_back(value);
    }

    void pop(int value) {
        // 현재 최대값이 빠지는 값이라면 제거
        if (!dq.empty() && dq.front() == value) {
            dq.pop_front();
        }
    }

    int max() {
        return dq.front();
    }
};


'''
