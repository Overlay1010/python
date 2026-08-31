def solution(my_string):
    answer = [0]*52
    for char in my_string:
        if 'a' <= char <= 'z':
            idx = ord(char) - ord('a')+ 26
            answer[idx] += 1
        elif 'A' <= char <= 'Z':
            idx = ord(char) - ord('A')
            answer[idx] += 1
    return answer