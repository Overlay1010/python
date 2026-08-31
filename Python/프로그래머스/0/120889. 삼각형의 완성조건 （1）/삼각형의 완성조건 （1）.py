def solution(sides):
    answer = 1
    sides.sort()
    if sides[-1] >= sides[0]+sides[1]:
        answer =2
    return answer