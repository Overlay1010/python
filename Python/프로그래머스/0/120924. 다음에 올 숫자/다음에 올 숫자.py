def solution(common):
    answer = 0
    if common[-1] - common[-2]  == common[-2] - common[-3]:
        a = common[-1] - common[-2]
        answer = common[-1] + a
    else:
        b = common[-1] / common[-2]
        answer = common[-1] * b
    return answer