# 수포자 3인방이 모의고사 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answers가 주어졌을 때 가장 많은 문제를 맞힌 사람이 누구인지
# 배열에 담아 반환하도록 solution() 함수를 작성하세요.

# 제약 조건
# 시험은 최대 10,000 문제로 구성
# 문제의 정답은 1, 2, 3, 4, 5 중 하나
# 가장 높은 점수를 받은 사람이 여럿이라면 반환하는 값을 오름차순으로 정렬하세요.

# 입출력의 예
# answers           return
# [1, 2, 3, 4, 5]   [1]
# [1, 3, 2, 4, 2]   [1, 2, 3]

# 문제 분석

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 수포자들의 점수를 저장할 리스트
    scores = [0] * 3

    # 각 수포자들의 패턴과 정답이 얼마나 일치하는지 확인
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1

    # 가장 높은 점수 저장
    max_score = max(scores)

    # 가장 높은 점수를 가진 수포자의 번호를 찾아서 리턴
    highest_scores = []
    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i + 1)
    return highest_scores


answers = list(map(int, input().split()))
print(solution(answers))