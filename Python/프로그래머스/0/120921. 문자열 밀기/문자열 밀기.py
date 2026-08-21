def solution(A, B):
    answer = -1
    B2 = B + B
    if A in B2:
        answer = B2.index(A)
        
    return answer