def solution(numbers, n):
    answer = 0
    total = 0
    for i in numbers:
        total+=i
        if total>n:
            answer = total
            break
    return answer