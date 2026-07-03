def solution(n):
    answer = []
    for i in list(str(n)):
        answer.append(int(i))
    answer = answer[::-1]
    return answer