def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if abs(arr[i]) % abs(divisor) == 0:
            answer.append(arr[i])
    answer.sort()
    return answer if len(answer) != 0 else [-1]