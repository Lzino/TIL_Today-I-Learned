# defaultdict 선언
from collections import defaultdict 

word = "life is good"
word_count = defaultdict(int)

for letter in word :
    word_count(letter) += 1

print(word_count)

# 정규 표현식
import re 
temp = re.split('[^0-9]', list)
## 숫자 빼고 추출하기 
## 그 외 : [^A-Z] 대문자가 아닌 모든 문자, [^abc] → a, b, c가 아닌 모든 문자

# 리스트를 문자열로 합치기
## ['a', 'b', 'c'] →  'abc'
temp = ''.join(list)

# SQL 주요 함수 
## 추출
ROW_NUMBER() OVER (PARTITION BY ■ ORDER BY ■ DESC) AS RN
## 날짜(DATE) 타입 변환
DATE_FORMAT, CAST( AS DATE), DATE()
## IF문 대신
CASE WHEN ■ THEN ■ ELSE END 
