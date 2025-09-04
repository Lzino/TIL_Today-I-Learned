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


'''
에라토스테네스의 체 (소수 구하기)
'''
import math
n = 1000
array = [True for i in range (n +1 )]

# 제곱근까지만 소수 알아보기
for i in range(2, math.sqrt(n) + 1):
    if array[i] == True :
        j = 2 # 2번째 배수부터
        while i * j <= n :
            array[i*j] = False # i를 제외한 배수들 다 지우기 
            j += 1
            
# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')


'''
누적합(prifix_sum) 만들기
'''

# 전체 데이터 선언
data = [10, 20, 30, 40, 50]


# 더해줄 변수와 누적합 리스트 선언  
sum_value = 0
prfix_sum= [0]

# 더할때마다 리스트 추가. DP땐 defaultdict 사 
for i in data:
    sum_value += i 
    prfix_sum.append(sum_value)

# 인덱스 기준 2번에서 3번사이의 합이 필요할때
left = 2
right = 3

print(prfix_sum[right] - prfix_sum[left-1])

'''
SQL 주요 함수 
'''
## 추출
ROW_NUMBER() OVER (PARTITION BY ■ ORDER BY ■ DESC) AS RN
## 날짜(DATE) 타입 변환
DATE_FORMAT, CAST( AS DATE), DATE()
## IF문 대신
CASE WHEN ■ THEN ■ ELSE END 
