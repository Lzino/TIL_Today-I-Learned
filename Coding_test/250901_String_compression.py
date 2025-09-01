# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def compress_with_k(s, k):
    """
    s를 길이 k로 잘라 압축한 문자열의 길이를 반환.
    실제 압축 문자열을 만들지 않고 길이만 계산해도 되지만,
    이해를 돕기 위해 문자열을 만들어본 뒤 len()을 씁니다.
    """
    pieces = []               # 압축 결과를 이어 붙일 버퍼
    prev = s[0:k]             # 직전 조각
    count = 1                 # prev가 몇 번 반복되었는지

    # k 간격으로 순회하며 조각 비교
    for i in range(k, len(s), k):
        cur = s[i:i+k]
        if cur == prev:
            count += 1
        else:
            # 지금까지의 prev를 압축해 pieces에 기록
            if count > 1:
                pieces.append(str(count))
            pieces.append(prev)
            # 현재 조각으로 초기화
            prev = cur
            count = 1

    # 마지막 prev도 반영
    if count > 1:
        pieces.append(str(count))
    pieces.append(prev)

    # 이어붙인 뒤 길이 반환
    return len("".join(pieces))


def solution(s):
    n = len(s)
    if n == 1:
        return 1

    answer = n  # 최댓값(압축 안 한 길이)으로 초기화
    # 가능한 모든 k 시도
    for k in range(1, n // 2 + 1):
        # 길이 k로 잘라 압축했을 때의 길이
        # 꼬리는 compress_with_k 내부에서 자동 처리됨(slicing이 남은 부분도 조각으로 들어감)
        compressed_len = compress_with_k(s, k)
        if compressed_len < answer:
            answer = compressed_len
    return answer


'''
또 다른 풀이
'''

def compress_with_k(s, k):
    prev = s[0:k]
    count = 1
    compressed = ""   # join 대신 문자열 누적

    for i in range(k, len(s), k):
        cur = s[i:i+k]
        if cur == prev:
            count += 1
        else:
            compressed += (str(count) + prev) if count > 1 else prev
            prev, count = cur, 1

    # 마지막 덩어리 처리
    compressed += (str(count) + prev) if count > 1 else prev

    return len(compressed)
