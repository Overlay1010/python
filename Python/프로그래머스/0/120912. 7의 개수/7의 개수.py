def solution(array):
    answer = 0
    a = ''
    for i in array:
        a+= str(i)
    for ch in a:
        if int(ch) == 7:
            answer+=1
    return answer