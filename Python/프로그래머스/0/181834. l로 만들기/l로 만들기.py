def solution(myString):
    answer = ''
    for i in myString:
        if i < 'l':
            i = 'l'
        answer +=i
    return answer