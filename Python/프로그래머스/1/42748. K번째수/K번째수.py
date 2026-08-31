def solution(array, commands):
    answer = []
    a = []
    for i in commands:
        a=array[int(i[0]-1):int(i[1])]
        a.sort()
        answer.append(a[i[2]-1])
    return answer