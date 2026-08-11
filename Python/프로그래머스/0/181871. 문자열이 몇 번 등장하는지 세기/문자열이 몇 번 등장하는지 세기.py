def solution(myString, pat):
    answer = 0
    a = ""
    n = len(pat)
    for i in (myString): 
        a+=i
        if a[-n:] == pat:
            answer+=1
    return answer