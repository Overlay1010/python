def solution(s):
    answer = 0
    s = list(s.split())
    for ch in range(len(s)):
        if s[ch] != 'Z':
            answer+= int(s[ch])
        else:
            answer -= int(s[ch-1])
    return answer