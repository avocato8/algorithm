# 두 개 뽑아서 더하기
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 2개의
# 수를 뽑아 더해 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환하는
# solution() 함수를 완성하세요.

# 제약 조건
# 1. numbers의 길이는 2 이상 100 이하입니다.
# 2. numbers의 모든 수는 0 이상 100 이하입니다.

# 문제 분석
# 1. 배열에서 두 수를 선택하는 모든 경우의 수를 구합니다.
# 2. 과정1에서 구한 수를 새로운 배열에 저장하고 중복값을 제거
# 3. 배열을 오름차순으로 정렬하고 반환

def solution(numbers):
    ret = []
    for i in range(len(numbers)):           # 두 수를 선택하는 모든 경우의 수를 구함
        for j in range(i + 1, len(numbers)):
            ret.append(numbers[i] + numbers[j])
    ret = sorted(set(ret))                  # 중복된 값을 제거하고 오름차순으로 정렬
    return ret

numbers = list(map(int, input().split()))
print(numbers)
result = solution(numbers)
print(result)
