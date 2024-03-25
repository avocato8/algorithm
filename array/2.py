# 배열 제어하기
# 문제 : 정수 배열을 하나 받습니다. 배열의 중복값을 제거하고 배열 데이터를
# 내림차순으로 정렬해서 반환하는 solution() 함수를 구현하세요.

# 제약 조건
# 배열 길이는 2 이상 1000 이하 입니다.
# 각 배열의 데이터 값은 -100,000 이상 100,000 이하입니다.

def solution(lst):
    unique_lst = list(set(lst)) # 중복값 제거, O(n)
    unique_lst.sort(reverse=True) # 내림차순 정렬, O(n*log(n))
    return unique_lst

# 시간 복잡도 O(n*log(n))
