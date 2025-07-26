# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choice):
	# 딕셔너리 생성 
	scores = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

	for i in range (len(survey)):
		first = survey[i][0] # 비동의 점수
		second =survey[i][1] # 동의 점수
		choice = choice[i]

		if choice == 4 :
			# 모르겠음 : 아무 점수 없음 
			continue

		## 점수 절대값 화 
		point = abs(4 - choice)
		# 2번 (비동의) : 4 - 2 = abs(2) = 2
		# 7번(매우동의) : 4 - 7 = abs(-3) = 3

		if choice < 4 :
			# 비동의일때 점수주기
			scores[first] += point
		else :
			# 동의일때 점수주기 
			scores[second] += point 

	# 최종 성격 문자열 저장
	result = ''

	for a,b in [('R','T'),('C','F'),('J','M'),('A','N')]:
		if scores[a] >= score[b]:
			result += a
		else :
			result += b
	return result 

'''
[C++버전]
#include <string>
#include <vector>
#include <map>
#include <cmath>   // abs 함수 사용
using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    // 1. 성격 유형 점수를 저장할 map 초기화
    map<char, int> scores = {
        {'R', 0}, {'T', 0},
        {'C', 0}, {'F', 0},
        {'J', 0}, {'M', 0},
        {'A', 0}, {'N', 0}
    };

    // 2. 설문 문항을 순회하며 점수 계산
    for (int i = 0; i < survey.size(); i++) {
        char first = survey[i][0];   // 비동의 시 점수 받을 성격
        char second = survey[i][1];  // 동의 시 점수 받을 성격
        int choice = choices[i];     // 사용자의 응답 (1~7)

        if (choice == 4) continue;   // 4번은 점수 없음

        int point = abs(4 - choice); // 4와의 거리 → 점수

        if (choice < 4) {
            scores[first] += point;  // 비동의 → 앞글자에 점수
        } else {
            scores[second] += point; // 동의 → 뒷글자에 점수
        }
    }

    // 3. 성격 지표별로 비교하여 최종 성격 유형 결정
    string result = "";
    vector<pair<char, char>> types = {
        {'R', 'T'}, {'C', 'F'},
        {'J', 'M'}, {'A', 'N'}
    };

    for (auto [a, b] : types) {
        if (scores[a] >= scores[b]) {
            result += a; // 같거나 더 높은 쪽 선택
        } else {
            result += b;
        }
    }

    // 4. 최종 결과 반환
    return result;
}
'''



