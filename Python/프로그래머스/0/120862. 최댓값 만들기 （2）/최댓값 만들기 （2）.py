def solution(numbers):
    answer = 0
    numbers.sort()
    a = numbers[-1] * numbers[-2]
    if abs(numbers[0] * numbers[1]) > a:
        answer = numbers[0]*numbers[1]
    else:
        answer = a
    return answer