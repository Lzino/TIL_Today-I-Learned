# https://leetcode.com/problems/minimum-window-substring/description/
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 타겟에 필요한 알파벳을 정리한 dict
        need = collections.Counter(t)
        # 타겟에 대한 카운트
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동하면서 필요한 글자 찾을때마다 줄여가기
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # 만약 기존 것보다 더 짧으면 갱신
                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
