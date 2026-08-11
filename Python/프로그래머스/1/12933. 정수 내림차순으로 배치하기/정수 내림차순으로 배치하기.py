def solution(n):
    answer = ""
    n =list(str(n))
    n.sort()
    n = n[::-1]
    answer = int("".join(n))
    
    return answer