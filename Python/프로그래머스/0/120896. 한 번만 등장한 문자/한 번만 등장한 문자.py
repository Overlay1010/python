def solution(s):
    answer = ''
    a = {}
    for i in s:
        if i not in a:
            a[i] = 1
        else:
             a[i] += 1
    for i in sorted(a):
        if a[i] == 1:
            answer+=i

    return answer