def solution(s):
    answer = True
    stack = []
    pair = {')' : '('}
    for ch in s:
        if ch in '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] != pair[ch]:
                return False
            stack.pop()
    if stack:
        return False
    return True