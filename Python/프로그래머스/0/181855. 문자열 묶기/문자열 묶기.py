def solution(strArr):
    a = [len(s) for s in strArr]
    return max(a.count(length) for length in set(a))
