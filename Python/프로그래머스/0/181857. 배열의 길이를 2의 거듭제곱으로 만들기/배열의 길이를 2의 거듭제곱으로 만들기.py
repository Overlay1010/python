def solution(arr):
    n = len(arr)
    zero = 1
    while zero < n:
        zero*=2
    return arr + [0] * (zero - n)