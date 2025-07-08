##### 1. 소수 계산 + 완전 탐색 #####
'''
문제
정수 N(1 ≤ N ≤ 1 000)과 정수 배열 A(1..N)가 주어진다.
서로 다른 두 인덱스 i < j에 대해 |A[i] − A[j]| 가 소수(prime)이 되는 쌍의 개수를 구하라.
힌트 : 에라토스테네스의 체
'''

# 단순 소수 구하기
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
    
#  에라토스테네스의 체
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

def Sieve(n,a,primes):
    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    return(primes)

def count_prime_pairs(nums):
    n = len(nums)
    max_diff = max(nums) - min(nums)

    # ---------- 1. 소수 테이블 ----------
    is_prime = [False, False] + [True] * (max_diff - 1)
    p = 2
    while p * p <= max_diff:
        if is_prime[p]:
            for multiple in range(p*p, max_diff+1, p):
                is_prime[multiple] = False
        p += 1

    # ---------- 2. 두 수씩 비교 ----------
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_prime[abs(nums[i] - nums[j])]:
                cnt += 1
    return cnt

##### 2. 문자열 처리 #####
'''
문제
한 문단의 영어 텍스트가 주어진다.
모든 사람 이름(PERSON) 엔티티를 동일 길이의 'X' 문자로 치환한 결과를 출력하라.
단, spaCy 모델(en_core_web_sm)만 사용 가능.

힌트 : 문자열 가공 + 인덱스 + spaCy 사용
'''
import sys, spacy
def anonymize(text: str) -> str:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    chars = list(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            for idx in range(ent.start_char, ent.end_char):
                # 공백·줄바꿈은 그대로 두고 글자만 X
                if not chars[idx].isspace():
                    chars[idx] = 'X'
    return "".join(chars)

if __name__ == "__main__":
    TC1 = 'Steve Jobs and Bill Gates changed the tech industry.'
    print(anonymize(TC1))

##### 3. Minimum Flips to Valid ID #####
'''
문제
길이가 N(≤ 100 000)인 대문자 문자열 S와 정수 K(1…26)가 주어진다.
S를 수정(아무 위치 글자를 다른 글자로 교체)해 다음 두 규칙을 모두 만족시키려 한다.

인접 문자가 모두 다르다.

모든 접두사에 대해 max_c cnt(c) − min_c cnt(c) ≤ K.
(cnt(c)는 접두사에서 문자 c 등장 횟수)
최소 교체 횟수를 출력하라.

예시 :
Input:
AAABBC
1

Output:
2

힌트 : 맞춤 자료구조 설계 + DP/그리디 + 조건 만족 최소수정
'''
## https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)          # 각 문자의 빈도수 계산
        used = set()               # 이미 사용된 빈도값 집합
        deletions = 0              # 삭제 횟수 누적

        for f in freq.values():    # 문자 자체는 중요하지 않고 빈도만 필요
            while f > 0 and f in used:
                f -= 1             # 빈도 1 감소 = 문자 1개 삭제
                deletions += 1
            used.add(f)            # 0도 포함 (0은 무시해도 중복 안 생김)

        return deletions

## https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # 하나 지워보기: 왼쪽 삭제 vs 오른쪽 삭제
                return is_pal(l + 1, r) or is_pal(l, r - 1)
        return True


## https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for ch in s:
            if len(res) >= 2 and res[-1] == res[-2] == ch:
                continue      # 3연속이면 건너뜀
            res.append(ch)
        return ''.join(res)


## https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description
class Solution:
    def minOperations(self, s: str) -> int:
        mismatchA = mismatchB = 0
        
        for i, ch in enumerate(s):
            expectedA = '0' if i % 2 == 0 else '1'  # "0101..." 패턴
            expectedB = '1' if i % 2 == 0 else '0'  # "1010..." 패턴
            
            if ch != expectedA:
                mismatchA += 1
            if ch != expectedB:
                mismatchB += 1
        
        return min(mismatchA, mismatchB)


## https://leetcode.com/problems/reorganize-string/description/?utm_source=chatgpt.com
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)

        # ① 불가능 조건
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # ② max-heap 준비 (파이썬은 min-heap → 빈도에 음수 부호)
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        res = []

        # ③ 두 문자씩 꺼내기
        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)   # 가장 많은 문자
            cnt2, ch2 = heapq.heappop(heap)   # 두 번째

            res.extend([ch1, ch2])

            # 사용 후 남으면 재삽입 (cnt는 음수임에 주의)
            if cnt1 + 1:          # cnt1은 음수 → +1은 빈도 1 감소
                heapq.heappush(heap, (cnt1 + 1, ch1))
            if cnt2 + 1:
                heapq.heappush(heap, (cnt2 + 1, ch2))

        # ④ 힙에 1개 남은 경우 처리
        if heap:
            cnt, ch = heap[0]     # (-1, 'x') 형태
            if res and res[-1] == ch:
                return ""         # 직전 문자와 충돌 → 불가능
            res.append(ch)

        return "".join(res)


