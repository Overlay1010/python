def solution(num, k):
    answer = -1
    num = str(num)
    if str(k) in num:
        answer = (num.index(str(k)))+1
        
    return answer