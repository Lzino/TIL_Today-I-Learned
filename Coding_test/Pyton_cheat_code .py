# defaultdict 선언
from collections import defaultdict 

word = "life is good"
word_count = defaultdict(int)

for letter in word :
    word_count(letter) += 1

print(word_count)

# 펠린드롬(회문)
## 방법 1 : 1대1 대응
for i in range(len(word)):
    if word[i] == word[len(word)-1-i]:
        print(1)
    else :
        print(0)

## 방법 2 : reversed(iterabla) 사용. reverse()는 None값 배출 (리스트만 바꿈) 
for i in range(len(word)):
    if word[i] == list(reversed(word)):
        print(1)

## 방법 3 : 문자열 슬라이싱
## 문자열 :  [start : end : step]
for i in range(len(word)):
    if word == word[::-1]: # 거꾸로 해보기
        print(1)

## 기타 방법 : 리스트의 pop(0) vs pop(), deque의 popleft() vs pop()


# 정규 표현식
import re 
temp = re.split('[^0-9]', list)
## 숫자 빼고 추출하기 
## 그 외 : [^A-Z] 대문자가 아닌 모든 문자, [^abc] → a, b, c가 아닌 모든 문자

# 리스트를 문자열로 합치기
## ['a', 'b', 'c'] →  'abc'
temp = ''.join(list)

# 에라토스테네스의 체 (소수 구하기)

# 누적합 만들기


# SQL 주요 함수 
## 추출
ROW_NUMBER() OVER (PARTITION BY ■ ORDER BY ■ DESC) AS RN
## 날짜(DATE) 타입 변환
DATE_FORMAT, CAST( AS DATE), DATE()
## IF문 대신
CASE WHEN ■ THEN ■ ELSE END 
