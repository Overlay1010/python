def solution(myString, pat):
    n = len(pat)
    answer = ''
    longest = None
    for i in myString:
        answer += i
        if answer[-n:] == pat:
            longest = answer   # 매칭될 때마다 계속 갱신 (return 하지 않음)
    return longest