import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 구하고자하는 문자열의 오른쪽과 왼쪽
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            # 왼쪽에서 오른쪽으로 한칸씩 이동
            counts[s[right - 1]] += 1

            # 가장 흔하게 등장하는 문자 탐색
            # 최대값 구하는 건 최적화를 위해 생략
            max_char_n = counts.most_common(1)[0][1]
            
            # 문자열의 오른쪽에서 왼쪽을 뺀 값의 최대값 = 가장 많이 나온 수 + K값이 되어야함
            # 그래서 오른쪽 주소 - 왼쪽 주소 - 가장 많이 나온 수 = K 가 됨 
            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left
