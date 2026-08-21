def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if all(n in '05' for n in str(i)):
            answer.append(i)
    return answer if answer else [-1]