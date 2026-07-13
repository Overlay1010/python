def solution(array, n):
    answer = 0
    a =[]
    array.sort()
    for i in array:
        a.append(abs(i-n))
    idx = a.index(min(a))        
    answer = array[idx]
    return answer