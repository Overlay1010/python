def solution(numbers, k):
    answer = 0
    a = []
    i=0
    while numbers:
        a.append(numbers[i])
        i+=2
        k-=1
        if i >= len(numbers):
            i= i % len(numbers)
        if k == 0:
            answer = a[-1]
            break
    return answer