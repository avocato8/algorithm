import time
# 정수 배열을 정렬해서 반환하는 solution() 함수를 완성하세요.

# 제약 조건
# 정수 배열의 길이는 2이상 10^5 이하
# 정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하입니다.

# 문제 분석
# 졔약 조건을 보면 데이터 개수는 최대 10^5개 이므로, 제한 시간이 3초이면 O(N^2) 알고리즘은
# 사용할 수 없다.

# 만약 O(N^2)인 버블 정렬로 구현하면?
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
    return arr

# sorted 함수로 배열 구현
def do_sort(arr):
    sorted_list = sorted(arr)
    return sorted_list

# 시간 측정하고 뒤집힌 배열 반환
def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result

# 첫 번째 코드 시간 측정
arr = list(range(10000))
bubble_time, bubble_result = measure_time(bubble_sort, arr)
print("첫 번째 코드 실행 시간: ", format(bubble_time, ".10f"))

# 두 번째 코드 시간 측정
arr = list(range(10000))
sorted_time, sorted_result = measure_time(do_sort, arr)
print("두 번째 코드 실행 시간: ", format(sorted_time, ".10f"))

#두 개의 코드가 동일한지 확인
print("두 개의 코드의 결과가 동일한지 확인:" , bubble_result == sorted_result)

