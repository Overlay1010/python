def solution(picture, k):
    answer = []
    a = ""
    for i in range(len(picture)):
        a = ""
        for j in picture[i]:
            a+= j*k
        for _ in range(k):
            answer.append(a)              
    return answer