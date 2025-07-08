##### 1. 소수 계산 + 완전 탐색 #####
'''
문제
정수 N(1 ≤ N ≤ 1 000)과 정수 배열 A(1..N)가 주어진다.
서로 다른 두 인덱스 i < j에 대해 |A[i] − A[j]| 가 소수(prime)이 되는 쌍의 개수를 구하라.

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

힌트 : 에라토스테네스의 체
'''

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
## https://leetcode.com/problems/valid-palindrome-ii/description/
## https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
## https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/
## https://leetcode.com/problems/reorganize-string/description/?utm_source=chatgpt.com

